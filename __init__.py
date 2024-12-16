from .node import SAM2ModelLoader, GroundingDinoModelLoader, GroundingDinoSAM2Segment, InvertMask, IsMaskEmptyNode

NODE_CLASS_MAPPINGS = {
    'SAM2ModelLoader (segment anything2)': SAM2ModelLoader,
    'GroundingDinoModelLoader (segment anything2)': GroundingDinoModelLoader,
    'GroundingDinoSAM2Segment (segment anything2)': GroundingDinoSAM2Segment,
    'InvertMask (segment anything2)': InvertMask,
    "IsMaskEmpty": IsMaskEmptyNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'SAM2ModelLoader (segment anything2)': 'SAM2 Model Loader (segment anything2)',
    'GroundingDinoModelLoader (segment anything2)': 'Grounding Dino Model Loader (segment anything2)',
    'GroundingDinoSAMSegment (segment anything2)': 'Grounding Dino SAM Segment (segment anything2)',
    'InvertMask (segment anything2)': 'Invert Mask (segment anything2)',
    "IsMaskEmpty": "Is Mask Empty",
}
