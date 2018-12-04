import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
    	&quot;&quot;&quot; Retrieve data from the input source and return an object&quot;&quot;&quot;
    	return
    
    @abc.abstractmethod
    def save(self, output, data):
    	&quot;&quot;&quot;Save the data object to the output&quot;&quot;&quot;
    	return

