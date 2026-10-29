"""Example data used by the local figure scripts."""

import numpy as np

data_comparison = {'methods': ['DPO', 'DA-DPO', 'VIGIL (Ours)'], 'colors': ['#D88F8A', '#8BCF8B', '#0F4D92'], 'results': {'Qwen2.5-VL-7B\nPOPE$_{Adv}$': np.array([82.8, 84.2, 86.9]), 'LLaVA-OneVision-7B\nPOPE$_{Adv}$': np.array([82.8, 84.2, 86.9]), 'InternVL2.5-26B\nPOPE$_{Adv}$': np.array([85.5, 86.8, 89.4]), 'Qwen2.5-VL-72B\nPOPE$_{Adv}$': np.array([84.5, 87.4, 89.8]), 'Qwen2.5-VL-7B\nMathVista': np.array([48.0, 48.8, 49.5]), 'LLaVA-OneVision-7B\nMathVista': np.array([50.8, 51.5, 52.8]), 'InternVL2.5-26B\nMathVista': np.array([57.9, 58.8, 60.1]), 'Qwen2.5-VL-72B\nMathVista': np.array([54.1, 55.4, 56.6]), 'Qwen2.5-VL-7B\nMMBench': np.array([71.2, 72.0, 72.5]), 'LLaVA-OneVision-7B\nMMBench': np.array([72.5, 73.0, 73.8]), 'InternVL2.5-26B\nMMBench': np.array([79.5, 80.1, 81.3]), 'Qwen2.5-VL-72B\nMMBench': np.array([77.2, 77.8, 78.5])}}
