'''OpenGL extension INGR.interlace_read

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_INGR_interlace_read'
_DEPRECATED = False
GL_INTERLACE_READ_INGR = constant.Constant( 'GL_INTERLACE_READ_INGR', 0x8568 )
glget.addGLGetConstant( GL_INTERLACE_READ_INGR, (1,) )


def glInitInterlaceReadINGR():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
