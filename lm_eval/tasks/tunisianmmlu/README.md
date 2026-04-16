# TunisianMMLU

### Paper

Title: TunisianMMLU: Evaluating Large Language Models on Tunisian Arabic

Abstract: TunisianMMLU is an evaluation benchmark designed to assess large language models' (LLM) performance in Tunisian Arabic. It consists of 22,027 multiple-choice questions, translated from selected subsets of the Massive Multitask Language Understanding (MMLU), ArabicMMLU and DarijaMMLU benchmarks to measure model performance.

Homepage: [https://huggingface.co/datasets/linagora/TunisianMMLU](https://huggingface.co/datasets/linagora/TunisianMMLU)


### Citation

```
@inproceedings{linagora2026LLM-tn,
      title={TunisianMMLU: Evaluating Large Language Models on Tunisian Arabic}, 
      author={Wajdi Ghezaiel and Jean-Pierre Lorré},
      year={2026},
}
```

### Groups and Tasks 

#### Groups

* `tunisianmmlu`: evaluates all TunisianMMLU tasks.

#### Tags
Source-based tags:

* `tunisianmmlu_mmlu`: evaluates TunisianMMLU tasks that were translated from MMLU.
* `tunisianmmlu_ar_mmlu`: evaluates TunisianMMLU tasks that were translated from ArabicMMLU.

Category-based tags:

* `tunisianmmlu_stem`: evaluates TunisianMMLU STEM tasks.
* `tunisianmmlu_social_sciences`: evaluates TunisianMMLU social sciences tasks.
* `tunisianmmlu_humanities`: evaluates TunisianMMLU humanities tasks.
* `tunisianmmlu_language`: evaluates TunisianMMLU language tasks.
* `tunisianmmlu_other`: evaluates other TunisianMMLU tasks.

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
