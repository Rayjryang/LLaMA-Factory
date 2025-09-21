export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
#llamafactory-cli train examples/train_full/qwen2_5vl_full_sft_occlusion.yaml 
# UV_PROJECT_ENVIRONMENT=~/venvs/llmf uv run --prerelease=allow llamafactory-cli train examples/train_full/qwen2_5vl_full_sft_occlusion.yaml 
UV_PROJECT_ENVIRONMENT=~/venvs/llmf uv run --prerelease=allow llamafactory-cli train examples/train_lora/qwen2_5vl_lora_sft_occ.yaml
#UV_PROJECT_ENVIRONMENT=~/venvs/llmf uv run --prerelease=allow llamafactory-cli export examples/merge_lora/qwen2_5vl_lora_sft_occ.yaml
