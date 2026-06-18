import os
import matplotlib.pyplot as plt


class BaseChart:

    OUTPUT_DIR = "output"

    @classmethod
    def save(cls, filename):
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        plt.tight_layout()

        plt.savefig(
            f"{cls.OUTPUT_DIR}/{filename}",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()