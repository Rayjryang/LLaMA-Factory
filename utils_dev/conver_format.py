import json
import os

def convert_llava_to_mllm_demo(input_file, output_file, image_base_dir):
    """
    Convert LLaVA format to mllm_demo format.
    
    Args:
        input_file: Path to the LLaVA format JSON file
        output_file: Path to save the converted mllm_demo format JSON file
        image_base_dir: Base directory for images
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        llava_data = json.load(f)
    
    mllm_data = []
    
    for item in llava_data:
        # Convert conversations to messages format
        messages = []
        for conv in item['conversations']:
            role = "user" if conv['from'] == "human" else "assistant"
            messages.append({
                "content": conv['value'],
                "role": role
            })
        
        # Create the new format entry
        mllm_entry = {
            "messages": messages,
            "images": [os.path.join(image_base_dir, item['image'])]
        }
        
        mllm_data.append(mllm_entry)
    
    # Save the converted data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mllm_data, f, ensure_ascii=False, indent=2)
    
    print(f"Converted {len(mllm_data)} entries from {input_file} to {output_file}")

if __name__ == "__main__":
    image_base_dir = "/mnt/localssd/sa2va/llava_data/llava_images"
    # "/mnt/localssd/datasets/v1/annotation_0806_full_train/edges"

    input_file = "/sensei-fs/users/jinruiy/code/occlusion/oc_related_works/Sa2VA/custom_data/llava_v1_5_mix665k_100k.json"
    json_name = os.path.basename(input_file)

    output_file = f"/sensei-fs/users/jinruiy/code/po_related_works/LLaMA-Factory/data/custom_configs/qwen_{json_name}"
    
    convert_llava_to_mllm_demo(input_file, output_file, image_base_dir)
