class Lora_Strength_Incrementer:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "step": 1}),
				"increment_step": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.001}),
				"start_strength": ("FLOAT", {"default": 0.0, "min": -50.0, "max": 50.0, "step": 0.01}),
				#"stop_at_strength": ("FLOAT", {"default": 5.0, "min": -50.0, "max": 50.0, "step": 0.01}), #idk how to do this 
            },
        }

    RETURN_TYPES = ("FLOAT", "STRING") 
    FUNCTION = "increment_strength"
    CATEGORY = "Right click lora loader and convert widget to input. Set control to increment. Start at seed = 0"
    
    def increment_strength(self, seed=0, increment_step=0.0, start_strength=0.0):#, stop_at_strength=0.0):  

        output = start_strength + seed * increment_step 
        return (float(output), str(output))

NODE_CLASS_MAPPINGS = {
    "Lora Strength Incrementer": Lora_Strength_Incrementer,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Lora Strength Incrementer": "Lora Strength Incrementer",
}