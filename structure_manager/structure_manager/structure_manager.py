# -*- coding: utf-8 -*-
"""
/***************************************************************************
 StructureManager
                                 A QGIS plugin
 Manage shapefiles and csv export
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-12-19
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Cary Hutchinson                   Revision  2018_1227
        email                : chutchinson@ssi-mi.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import csv
from qgis.core import QgsVectorLayer, QgsField, QgsProject, QgsFeature, QgsPoint, QgsGeometry, QgsPointXY
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt, QVariant
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMessageBox, QFileDialog

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .structure_manager_dialog import StructureManagerDialog
import os.path


class StructureManager:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'StructureManager_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = StructureManagerDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&SSI Structure Manager')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'StructureManager')
        self.toolbar.setObjectName(u'StructureManager')

        self.home = os.getenv("HOME")
        self.local_dir = os.getenv("HOME")
        self.jobnum = "NULL"
        self.pipe_layer = "NULL"
        self.struct_layer = "NULL"

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('StructureManager', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/structure_manager/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'SSI Structure Manager'),
            callback=self.run,
            parent=self.iface.mainWindow())

            
        self.dlg.pb_setup_shape.clicked.connect(self.setup_shape) 
        self.dlg.pb_format_all.clicked.connect(self.format_all) 
        self.dlg.pb_export_csv.clicked.connect(self.export_csv) 
        self.dlg.linEd_csv_file.returnPressed.connect(self.export_csv)
        self.dlg.button_box.accepted.connect(self.accept_button)
        self.dlg.button_box.rejected.connect(self.accept_button)

    def select_pipes(self):#***********************************   NOT WORKING YET ****************************************
        layer = self.iface.activeLayer()
        layer_name = str(layer.name())
        name_split = layer_name.split("_")
        self.jobnum = name_split[0]
        self.dlg.label_jobnumber.setText(self.jobnum)
        if 'PIPES' in name_split[1]:
            self.dlg.label_layername.setText(layer_name)
            self.pipe_layer = layer_name
            self.dlg.textBrowser.append(layer_name )
        else:
            self.popMsg('Choose a layer with PIPES only. ' + layer_name)
            return
        


    def setup_shape(self):#***********************************   NOT WORKING YET ****************************************
        openfile = QFileDialog.getOpenFileName(None, "Pick Structure Shape File", self.local_dir, "Shape File (*.shp)")           
        self.dlg.label_shapefile.setText(openfile[0]) 
        name = openfile[0]
        self.jobnum = name.split('_')[0]
        self.pipe_layer = self.jobnum + '_PIPES'
        self.dlg.label_layername.setText(self.pipe_layer)
        self.dlg.label_jobnumber.setText(self.jobnum)
        ''' import this shape file 
            iterate through the attributes and look for correct attribute names
            add the missing attributes.
            add time.time to "UPDATE"
            Generate PIPES layer
            '''
    
    def make_pipe_layer(self):
        self.add_fields_pipe()

    def add_fields_structure(self):

        layer = self.iface.activeLayer()
        layer_provider = layer.dataProvider()
        layer_provider.addAttributes([QgsField("YOURNAME",QVariant.String)])
        layer_provider.addAttributes([QgsField("SUMPDIST",QVariant.String)])
        
        layer_provider.addAttributes([QgsField("UPDATE",QVariant.String)])
        layer_provider.addAttributes([QgsField("LID",QVariant.String)])
        layer_provider.addAttributes([QgsField("NOTES",QVariant.String)])
        layer.updateFields()

    def add_fields_pipe(self):

        layer = self.iface.activeLayer()
        layer_provider = layer.dataProvider()
        layer_provider.addAttributes([QgsField("name",QVariant.String)])
        layer_provider.addAttributes([QgsField("jobnum",QVariant.String)])
        layer_provider.addAttributes([QgsField('invt_start',QVariant.String)]) 
        layer_provider.addAttributes([QgsField('invt_end',QVariant.String)])        
        layer_provider.addAttributes([QgsField("material",QVariant.String)])
        layer_provider.addAttributes([QgsField("start",QVariant.String)])
        layer_provider.addAttributes([QgsField("end",QVariant.String)])
        layer_provider.addAttributes([QgsField("update",QVariant.String)])
        layer_provider.addAttributes([QgsField("yourname",QVariant.String)])
        layer_provider.addAttributes([QgsField("status",QVariant.String)])
        layer_provider.addAttributes([QgsField("diameter",QVariant.String)])
        layer_provider.addAttributes([QgsField("ellipwidth",QVariant.String)])
        layer_provider.addAttributes([QgsField("stub_ang",QVariant.String)])
       
        layer.updateFields()


        

    def format_all(self):#***********************************   NOT WORKING YET ****************************************
        self.popMsg('Not working yet')
        return
    def export_csv(self):#***********************************   NOT WORKING YET ****************************************
        if len(self.dlg.linEd_csv_file.text()) < 2:
            self.popMsg('Plese input a longer file name.')
            return
        else:
            self.select_pipes()

        csv_dir = QFileDialog.getExistingDirectory(None, "Open a folder", self.local_dir, QFileDialog.ShowDirsOnly)
        csv_filename = self.dlg.linEd_csv_file.text()
        csv_filepath = str(csv_dir)+ '/' + csv_filename + '.csv'
        self.dlg.label_csv_filename.setText(csv_filepath)
        self.dlg.textBrowser.append(csv_filename )
        pipe_lyr = QgsProject.instance().mapLayersByName(self.pipe_layer)[0]
        if not pipe_lyr.isValid():
            self.popMsg('Layer is not valid')

        features = pipe_lyr.getFeatures()
        #Open CSV file here with with
        with open(csv_filepath, 'w', newline = '') as outfile:
            csv_writer = csv.writer(outfile, delimiter=',')
            i = int(800000)
            for pipe in features:  
                row1 = []
                row2 = []    
                #xx1 = pipe['invt_start']
                #xx1 = pipe['invt_end']
                #xx1 = pipe['start']
                #xx1= pipe['end']
                #xx1 = pipe['status']
                #xx1 = pipe['stub_ang']

                name = str(pipe['name'])
                material = str(pipe['material'])
                drain = str(pipe['drain'])
                dia = str(pipe['diameter'])
                diameter = dia.split('.')[0]
                ellipwidth= str(pipe['ellipwidth'])
                
                geom = pipe.geometry()
                line = geom.constGet() #line returns a QgsLineString object
            
                x0 = line.xAt(0) # x value of first vertex
                y0 = line.yAt(0) # y value of first vertex
                z0 = line.zAt(0) # z value of first vertex
                x1 = line.xAt(1) # x value of 2nd vertex
                y1 = line.yAt(1) # y value of 2nd vertex
                z1 = line.zAt(1) # z value of 2nd vertex '{0:.3f}'.format(k)
                if z0 < z1:
                    x1f = '{0:.3f}'.format(x1)
                    y1f = '{0:.3f}'.format(y1)
                    z1f = '{0:.3f}'.format(z1)
                    x2f = '{0:.3f}'.format(x0)
                    y2f = '{0:.3f}'.format(y0)
                    z2f = '{0:.3f}'.format(z0)
                else:
                    x1f = '{0:.3f}'.format(x0)
                    y1f = '{0:.3f}'.format(y0)
                    z1f = '{0:.3f}'.format(z0)
                    x2f = '{0:.3f}'.format(x1)
                    y2f = '{0:.3f}'.format(y1)
                    z2f = '{0:.3f}'.format(z1)
                    drain1 = drain + '_' + diameter
                    drain2 = drain + '_' + diameter
                    if not ellipwidth.isdigit():
                        eliptical = ''
                        start_desc = 'start--' + diameter +'IN ' + material
                        end_desc = 'end--' + diameter +'IN ' + material
                        
                    else:
                        eliptical = 'eliptical'
                        drain1 = drain1 + 'X' + str(ellipwidth)
                        drain2 = drain2 + 'X' + str(ellipwidth)
                        start_desc = 'start--' + diameter + 'X' + str(ellipwidth) +'IN ' + material
                        end_desc = 'end--' + diameter + 'X' + str(ellipwidth) +'IN ' + material

                    row1 = (i, x1f, y1f, z1f, drain1, start_desc, eliptical, name)
                    row2 = (i+1, x2f, y2f, z2f, drain2, end_desc, eliptical)
                    
                csv_writer.writerow(row1)
                csv_writer.writerow(row2)
                i = i + 2
        
        outfile.close()
      
        self.popMsg('Made through the csv creation')
        return

    def accept_button(self):
        self.popMsg('Not working yet')
        return

    def popMsg(self,text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec_()



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&SSI Structure Manager'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
