"""
Take in a YAML, and output all "other" splits with this YAML
"""

import argparse
import logging
import os

import yaml
from tqdm import tqdm


eval_logger = logging.getLogger("lm-eval")



SUBJECTS = {
    
    "high_school_european_history": "humanities",    
    "high_school_world_history": "humanities",
    "international_law": "humanities",
    "jurisprudence": "humanities",
    "logical_fallacies": "humanities",    
    "moral_disputes": "humanities",
    #"moral_scenarios": "humanities",    
    "philosophy": "humanities",
    "professional_law": "humanities",    
    "world_religions": "humanities",
    "islamic_studies": "humanities",
    "history": "humanities",
    "global_facts": "other",    
    "human_aging": "other",    
    "management": "other",
    "marketing": "other",    
    "nutrition": "other",  
    "driving_test": "other",  
    "general_knowledge": "other",
    "management_ar": "other",
    "history": "humanities",
    "law": "humanities",
    "philosophy_ar": "humanities",    
    "high_school_geography": "social_sciences",
    "high_school_government_and_politics": "social_sciences",
    "high_school_psychology": "social_sciences",    
    "professional_psychology": "social_sciences",
    "public_relations": "social_sciences",
    "security_studies": "social_sciences",
    "sociology": "social_sciences",
    "social_science": "social_sciences",
    "political_science": "social_sciences",    
    "accounting": "social_sciences",
    "geography": "social_sciences",
    "economics": "social_sciences",
    "civics": "social_sciences",    
    "high_school_statistics": "stem",
     "natural_science": "stem",    
    "physics": "stem",
    "computer_science": "stem",    
    "math": "stem",
    "biology": "stem",    
    "arabic_language": "language",    
    "arabic_language_(general)": "language",
    "arabic_language_(grammar)": "language",
    
}



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path", default="_default_tunisianmmlu_template_yaml")
    parser.add_argument("--save_prefix_path", default="tunisianmmlu")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # get filename of base_yaml so we can `"include": ` it in our "other" YAMLs.
    base_yaml_name = os.path.split(args.base_yaml_path)[-1]
    with open(args.base_yaml_path, encoding="utf-8") as f:
        base_yaml = yaml.full_load(f)

    ALL_CATEGORIES = []
    for subject, category in tqdm(SUBJECTS.items()):
        if category not in ALL_CATEGORIES:
            ALL_CATEGORIES.append(category)

        # description = f"The following are multiple choice questions (with answers) about {' '.join(subject.split('_'))}.\n\n"

        yaml_dict = {
            "include": base_yaml_name,
            "tag": f"tunisianmmlu_{category}",
            "task": f"tunisianmmlu_{subject.lower().replace(' ', '_')}",
            "task_alias": subject,
            "dataset_name": subject,
            # "description": description,
        }

        file_save_path = (
            args.save_prefix_path
            + f"_{subject.lower().replace(' ', '_').replace('(', '').replace(')', '')}.yaml"
        )
        eval_logger.info(f"Saving yaml for subset {subject} to {file_save_path}")
        with open(file_save_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                allow_unicode=True,
                default_style='"',
            )

    tunisianmmlu_subcategories = [f"tunisianmmlu_{category}" for category in ALL_CATEGORIES]

    file_save_path = args.save_prefix_path + ".yaml"

    eval_logger.info(f"Saving benchmark config to {file_save_path}")
    with open(file_save_path, "w", encoding="utf-8") as yaml_file:
        yaml.dump(
            {
                "group": "tunisianmmlu",
                "task": tunisianmmlu_subcategories,
            },
            yaml_file,
            indent=4,
            default_flow_style=False,
        )
