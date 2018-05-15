import sys
import redis
import os
import polib
import xml.etree.ElementTree as ET
import inspect
import collections

DEBUGPRINT = False
DEBUGPRINT_FUNCTIONS = False
DEBUGPRINT_ATTRIBUTE_GET = False
DEBUGPRINT_ATTRIBUTE_SET = False
     
def debugprint(msg):
    if DEBUGPRINT:
        print(msg)

def createMethodCallDebugString(classInstance, functionname, *args, **kwargs):
    function = object.__getattribute__(classInstance, functionname)
    myclass = object.__getattribute__( classInstance, "__class__")
    parentclass = myclass.__bases__[0]
    myclassname = myclass.__name__
    fromStub = ((functionname in vars(parentclass)) and (functionname not in vars(myclass)) )
    if fromStub == True:
        myclassname = "%sStub" % myclassname
        
    #print(functionname)
    #print(inspect.getargspec(function))
    #print(inspect.getargvalues(inspect.currentframe()))
    spec_args,       spec_varargs_name,    spec_varkw_name,    spec_default  = inspect.getargspec(function)
    current_args, current_varargs_name, current_varkw_name, current_locals = inspect.getargvalues(inspect.currentframe())
    
    current_local_args = current_locals[current_varargs_name]
    current_local_kwargs = current_locals[current_varkw_name]
    #print("Spec default" , spec_default)
    #print("Current local args", current_local_args)
    #print("Current local kwargs", current_local_kwargs)
    
    index = 0
    if spec_default != None:
        defaultindexoffset = len(current_local_args) - len(spec_default) + 1
    else:
        defaultindexoffset = 0
    #print("defaultindexoffset %s" % defaultindexoffset)
    debugstring = []   
    debugstring.append("%s:%s.%s(" % (
        inspect.getfile(myclass).split("/")[-1].split(".py")[0],
        myclassname,
        functionname,
    ))
    debugstringParams = []
    if len(spec_args) > 1:
        for index, arg in enumerate(spec_args[1:]):
            try:
                if arg in current_local_kwargs:
                    obj = current_local_kwargs[arg]
                    del  current_local_kwargs[arg]
                    try:
                        debugstringParams.append("%s=%s" % ( arg, obj.__repr__()))
                    except:
                        debugstringParams.append("%s=%s" % ( arg, obj))
                else:
                    obj = current_local_args[index]
                    try:
                        debugstringParams.append("%s=%s" % ( arg, obj.__repr__()))
                    except:
                        debugstringParams.append("%s=%s" % ( arg, obj))
            except Exception as e :
                #print(e)
                newindex = -1 - (len(spec_args)-index -2  )
                #print("newindex %s" % newindex)
                obj = spec_default[newindex ]
                debugstringParams.append("%s==%s" % (arg, obj.__repr__()))
    if len(current_local_args) > index+1:
        debugstringParams.append("*%s=%s" % (spec_varargs_name, current_local_args[index+1:].__repr__()))
        
    if len(current_local_kwargs.keys()) > 0:
        debugstringParams.append("**%s=%s" % (spec_varkw_name,current_local_kwargs))
            
    debugstring.append(", ".join( debugstringParams))
    debugstring.append(')')        
    return "".join(debugstring)

def createAttributeGetDebugString(classInstance, attributeName, attributeValue):
    myclass = object.__getattribute__( classInstance, "__class__")
    parentclass = myclass.__bases__[0]
    myclassname = myclass.__name__
    debugstring = "%s:%s.%s -> %s" % (inspect.getfile(myclass).split("/")[-1].split(".py")[0], myclassname, attributeName, attributeValue.__repr__())
    return debugstring
       
def createModuleMethodCallDebugString(module, functionname, function, fromStub,  *args, **kwargs):
    filename = inspect.getfile(function).split("/")[-1].split(".py")[0]
    if fromStub == True:
        filename = "%sStub" % filename
    #print("functionname: %s" % functionname)
    #print(inspect.getargspec(function))
    #print(inspect.getargvalues(inspect.currentframe()))
    spec_args,       spec_varargs_name,    spec_varkw_name,    spec_default  = inspect.getargspec(function)
    current_args, current_varargs_name, current_varkw_name, current_locals = inspect.getargvalues(inspect.currentframe())
    
    current_local_args = current_locals[current_varargs_name]
    current_local_kwargs = current_locals[current_varkw_name]
    #print("Spec default" , spec_default)
    #print("Current local args", current_local_args)
    #print("Current local kwargs", current_local_kwargs)
    #print("len(current_local_args)",len(current_local_args))
    
    
    index = 0
    if spec_default != None:
        defaultindexoffset = len(current_local_args) - len(spec_default)
    else:
        defaultindexoffset = 0
    #print("defaultindexoffset %s" % defaultindexoffset)
    debugstring = []   
    debugstring.append("%s:%s(" % (
        filename,
        functionname,
    ))
    debugstringParams = []
    if len(spec_args) > 0:
        for index, arg in enumerate(spec_args):
            try:
                if arg in current_local_kwargs:
                    obj = current_local_kwargs[arg]
                    del  current_local_kwargs[arg]
                    debugstringParams.append("%s=%s" % ( arg, obj.__repr__()))
                else:
                    obj = current_local_args[index]
                    debugstringParams.append("%s=%s" % ( arg, obj.__repr__()))
            except Exception as e :
                newindex = -1 - (len(spec_args)-index -1  )
                obj = spec_default[newindex ]
                debugstringParams.append("%s==%s" % (arg, obj.__repr__()))
    
    if len(current_local_args) > index+1:
        debugstringParams.append("*%s=%s" % (spec_varargs_name, current_local_args[index+1:].__repr__()))
        
    if len(current_local_kwargs.keys()) > 0:
        debugstringParams.append("**%s=%s" % (spec_varkw_name,current_local_kwargs))
            
    debugstring.append(", ".join( debugstringParams))
    debugstring.append(')')        
    return "".join(debugstring)
       
def debugPrintGetAttribute(classInstance, name):
    attr = object.__getattribute__(classInstance, name)
    if hasattr(attr, '__call__') and isinstance(attr, collections.Callable):    
        def f(*args, **kwargs):            
            result = attr(*args, **kwargs)
            if DEBUGPRINT_FUNCTIONS == True and not name.startswith("__"):
                s = createMethodCallDebugString(classInstance, name, *args, **kwargs)
                print("%s\n  return %s" % (s, result.__repr__() ))
            return result   
        return f
    else:
        if DEBUGPRINT_ATTRIBUTE_GET == True:
            print(createAttributeGetDebugString(classInstance, name, attr))
        return attr 
        
def debugPrintSetAttribute(classInstance, name, value):
        object.__setattr__(classInstance,name,value)
        myclass = object.__getattribute__( classInstance, "__class__")
        parentclass = myclass.__bases__[0]
        myclassname = myclass.__name__
        if DEBUGPRINT_ATTRIBUTE_SET == True:
            try:
                r = value.__repr__()
            except:
                try:
                    r = "%s" % value
                except: 
                    r = "__unresolved__"
            debugstring = "%s:%s.%s = %s" % (inspect.getfile(myclass).split("/")[-1].split(".py")[0], myclassname, name, r)
            print(debugstring)
  
def debugPrintInit(classInstance, *args, **kwargs):
    if DEBUGPRINT_FUNCTIONS == True:
        print(createMethodCallDebugString(classInstance, "__init__", *args, **kwargs))
                
def debugPrintModuleFunction(module, functionname, function, fromStub):
    attr = getattr(module, functionname)
    def f(*args, **kwargs):            
        s = createModuleMethodCallDebugString(module, functionname, function, fromStub, *args, **kwargs)
        result = attr(*args, **kwargs)
        if DEBUGPRINT_FUNCTIONS == True:
            print("%s\n  return %s" % (s, result.__repr__() ))
        return result   
    return f  

def initModuleMethodDebug(targetModule, stubModule):
    for name in dir(stubModule):
        if inspect.isfunction(getattr(stubModule, name)):
            #print(targetModule)
            attr = getattr(targetModule, name)
            if sys.modules[attr.__module__] == targetModule:
                #print("%s is function in %s" % (name, targetModule))
                setattr(targetModule, name, debugPrintModuleFunction(targetModule, name, attr, False))
            else:
                #print("module %s has no method %s, but stub has" % (targetModule,name))
                setattr(targetModule, name, debugPrintModuleFunction(stubModule, name, attr, True))
       