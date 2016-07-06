Standard Surface
*********

Inputs:

Surface Color:
	- GLOBAL VALUE: Controls the global color of your material. Works for all shading models except for those using Glass Dispersion and SSS.

Surface Metallic:
	- GLOBAL VALUE: Control the metallicness of your material. Typically used with a Metallic Texture. Metallic textures should be highest contrast possible. When using the Metallic Shading Model, plug in a metallic map into the Surface Metallic input. Use the Output on the other side of the node to mix between Dielectric and Metallic shading models. To do this, plug the Surface Metallic output into the Fac Input of a Mix Node.

Surface Roughness: 
	- GLOBAL VALUE: Controls the roughness of your material. Typically used with a roughness texture. Plug in a Roughness Map from the ONELVXE Texturing.Surface node.

Surface Normal:
	- GLOBAL VALUE: Controls the normal mapping of your material. Typically used with a normal texture. Plug in a Normal Map from the ONELVXE Texture.Surface node. 

Metallic Rim:
	- Controls the rim color when using Metallic Shading

Other Options:
	- Specific to which shading model you are currently using. Self explanatory.


Outputs:

Shaders:
	- Mix between different shading outputs or add them together using mix nodes and shader nodes. Typical use is one Shader Output at a time, i.e. Dielectric, Metallic, etc...

.. sidebar:: Screenshot [Surface.Standard]

   .. image:: surface_standard.jpeg	