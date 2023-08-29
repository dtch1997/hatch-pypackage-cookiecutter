"""Configuration for running {{ cookiecutter.package_name }}.main """
import ml_collections


def get_config():
    config = ml_collections.ConfigDict()
    config.seed = 0

    # WandB parameters
    config.track = False
    config.wandb_project = "{{ cookiecutter.package_name }}"
    config.wandb_entity = "{{ cookiecutter.github_username }}"
    config.wandb_name = None

    return config


def get_sweep(h):
    del h
    sweep = []
    for seed in [0, 1, 2]:
        sweep.append(
            {
                "config.seed": seed,
            }
        )
    return sweep