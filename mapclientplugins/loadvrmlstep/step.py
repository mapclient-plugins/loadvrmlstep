'''
MAP Client Plugin Step
'''
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.loadvrmlstep.configuredialog import ConfigureDialog

#from gias.common import simplemesh_tools
from gias2.mesh import simplemesh



class LoadVRMLStep(WorkflowStepMountPoint):
    '''
    Step for loading vertex coordinates and triangles from
    a vrml file on disk.
    '''

    def __init__(self, location):
        super(LoadVRMLStep, self).__init__('Load VRML', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'python#string'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'numpy#array3d'))
        self._config = {}
        self._config['identifier'] = ''
        self._config['filename'] = '.wrl'
        self._config['model index'] = '0'

        self._V = None
        self._T = None
        self._filename = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._filename == None:
            filename = self._config['filename']
        else:
            filename = self._filename

        #S = simplemesh_tools.vrml2SimpleMesh(filename)
        S = simplemesh.vrml_2_simple_mesh(filename)
        s = S[int(self._config['model index'])]
        self._V = s.v.copy()
        self._T = s.f.copy()
        self._doneExecution()

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 1:
            return self._V
        elif index == 2:
            return self._T

    def setPortData(self, index, dataIn):
        if index == 0:
            self._filename = dataIn

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
