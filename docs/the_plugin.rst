Material Pipeline
********************

The ONELVXE Material Pipeline is composed of 3 Main Parts:

    1. Texture Library w/ 100 Materials
    2. Texture Bridge
    3. Studio Shader


Texture/Material Library
=========

100 Textures and Materials for use in 3D Content Creation.

Main Features:

    1. Physically Based Rendering (PBR)
    
        - All of the textures have been fine tuned for PBR. The supported PBR texturing model is Roughness/Metallic mapping. For more information on the differing types of texturing workflows and how you can best leverage them as an artist go here: `PBR Guide <https://www.allegorithmic.com/pbr-guide>`_
        
    2. Seamless 4k, 2k, 1k resolutions
    3. Compatibility with any rendering engine or game engine that supports PBR
    4. Albedo, Roughness, Metallic, Normal, AO and Displacement Maps for every material
    5. Direct integration with Blender Cycles through library linking, appending or the ONELVXE Texture Bridge
    

Texture Bridge
=================

Multi-Texture Import Script:

Main Features:
    
    1. Import Entire set of textures via folder path
    2. Creates a node group of all of your textures
        
        - Connects image node vector input socket to group input socket
        - Names all Image Texture Nodes according to what type of texture map it is
        - Automatically sets the image nodes to Color Data or Non-Color Data depending upon texture map type
        
    3. Handles both Roughness/Metallic and Specular/Glossy Workflows
    4. Easy loading of new maps and refreshing of current texture maps
