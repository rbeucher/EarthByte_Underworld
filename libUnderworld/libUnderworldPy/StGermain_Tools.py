# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_StGermain_Tools', [dirname(__file__)])
        except ImportError:
            import _StGermain_Tools
            return _StGermain_Tools
        if fp is not None:
            try:
                _mod = imp.load_module('_StGermain_Tools', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _StGermain_Tools = swig_import_helper()
    del swig_import_helper
else:
    import _StGermain_Tools
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import StGermain
class StgData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StgData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StgData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["commworld"] = _StGermain_Tools.StgData_commworld_set
    __swig_getmethods__["commworld"] = _StGermain_Tools.StgData_commworld_get
    if _newclass:commworld = _swig_property(_StGermain_Tools.StgData_commworld_get, _StGermain_Tools.StgData_commworld_set)
    __swig_setmethods__["rank"] = _StGermain_Tools.StgData_rank_set
    __swig_getmethods__["rank"] = _StGermain_Tools.StgData_rank_get
    if _newclass:rank = _swig_property(_StGermain_Tools.StgData_rank_get, _StGermain_Tools.StgData_rank_set)
    __swig_setmethods__["nProcs"] = _StGermain_Tools.StgData_nProcs_set
    __swig_getmethods__["nProcs"] = _StGermain_Tools.StgData_nProcs_get
    if _newclass:nProcs = _swig_property(_StGermain_Tools.StgData_nProcs_get, _StGermain_Tools.StgData_nProcs_set)
    __swig_setmethods__["dictionary"] = _StGermain_Tools.StgData_dictionary_set
    __swig_getmethods__["dictionary"] = _StGermain_Tools.StgData_dictionary_get
    if _newclass:dictionary = _swig_property(_StGermain_Tools.StgData_dictionary_get, _StGermain_Tools.StgData_dictionary_set)
    __swig_setmethods__["argcCpy"] = _StGermain_Tools.StgData_argcCpy_set
    __swig_getmethods__["argcCpy"] = _StGermain_Tools.StgData_argcCpy_get
    if _newclass:argcCpy = _swig_property(_StGermain_Tools.StgData_argcCpy_get, _StGermain_Tools.StgData_argcCpy_set)
    __swig_setmethods__["argvCpy"] = _StGermain_Tools.StgData_argvCpy_set
    __swig_getmethods__["argvCpy"] = _StGermain_Tools.StgData_argvCpy_get
    if _newclass:argvCpy = _swig_property(_StGermain_Tools.StgData_argvCpy_get, _StGermain_Tools.StgData_argvCpy_set)
    def __init__(self): 
        this = _StGermain_Tools.new_StgData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _StGermain_Tools.delete_StgData
    __del__ = lambda self : None;
StgData_swigregister = _StGermain_Tools.StgData_swigregister
StgData_swigregister(StgData)


def StgInit(*args):
  return _StGermain_Tools.StgInit(*args)
StgInit = _StGermain_Tools.StgInit

def StgFinalise(*args):
  return _StGermain_Tools.StgFinalise(*args)
StgFinalise = _StGermain_Tools.StgFinalise
# This file is compatible with both classic and new-style classes.


