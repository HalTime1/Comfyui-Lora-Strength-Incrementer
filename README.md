HOW TO USE

Right click your "Load LoRA" node

Click "Convert Widget to Input"

Click "Convert strength_model" to input

Now connect "FLOAT" from the strength incrementer to "strength_model" on the lora loader.

Make sure "control_after_generate" is set to increment.

The ways this works is: start_strength + seed * increment_step.

You can set "increment_step" to a negative number while keeping "control_after_generate" set to increment.

Now auto-queue away!

If you want to temporarily not use the incrementer, set "increment_step" to 0 and use "start_strength" to change the strength.

Example video:
https://www.reddit.com/r/comfyui/comments/1hsbz2b/lora_strength_incrementer_custom_node/

This link also contains a comment suggesting using "queue trigger (countdown)" from impactpack.
Go give them an upvote!
