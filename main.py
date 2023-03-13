{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOM0lEYq6PZL+XZIxT+Qqv3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU",
    "gpuClass": "standard"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nabidhn/hello/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install flask"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "So2qhL8FfWIy",
        "outputId": "75aa2567-330d-4e53-cfea-210e6d4a99b1"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.9/dist-packages (2.2.3)\n",
            "Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.9/dist-packages (from flask) (6.0.0)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.9/dist-packages (from flask) (8.1.3)\n",
            "Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.9/dist-packages (from flask) (2.2.3)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.9/dist-packages (from flask) (2.1.2)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.9/dist-packages (from flask) (3.1.2)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata>=3.6.0->flask) (3.15.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from Jinja2>=3.0->flask) (2.1.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install flask-ngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ATMQpXaHfj8D",
        "outputId": "ef792a2f-5df1-431c-b1ba-7f18884adde1"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting flask-ngrok\n",
            "  Downloading flask_ngrok-0.0.25-py3-none-any.whl (3.1 kB)\n",
            "Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.9/dist-packages (from flask-ngrok) (2.2.3)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from flask-ngrok) (2.25.1)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask-ngrok) (2.1.2)\n",
            "Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask-ngrok) (6.0.0)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask-ngrok) (8.1.3)\n",
            "Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask-ngrok) (2.2.3)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.9/dist-packages (from Flask>=0.8->flask-ngrok) (3.1.2)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests->flask-ngrok) (2022.12.7)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->flask-ngrok) (1.26.14)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.9/dist-packages (from requests->flask-ngrok) (4.0.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->flask-ngrok) (2.10)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata>=3.6.0->Flask>=0.8->flask-ngrok) (3.15.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from Jinja2>=3.0->Flask>=0.8->flask-ngrok) (2.1.2)\n",
            "Installing collected packages: flask-ngrok\n",
            "Successfully installed flask-ngrok-0.0.25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install diffusers==0.10.2 transformers scipy ftfy accelerate\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kRcMwYhmgCD6",
        "outputId": "fb33a213-63af-4e8e-f03f-7b2690882ff1"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting diffusers==0.10.2\n",
            "  Downloading diffusers-0.10.2-py3-none-any.whl (503 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m503.1/503.1 KB\u001b[0m \u001b[31m10.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting transformers\n",
            "  Downloading transformers-4.26.1-py3-none-any.whl (6.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.3/6.3 MB\u001b[0m \u001b[31m65.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: scipy in /usr/local/lib/python3.9/dist-packages (1.10.1)\n",
            "Collecting ftfy\n",
            "  Downloading ftfy-6.1.1-py3-none-any.whl (53 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.1/53.1 KB\u001b[0m \u001b[31m7.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting accelerate\n",
            "  Downloading accelerate-0.17.0-py3-none-any.whl (212 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m212.8/212.8 KB\u001b[0m \u001b[31m20.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: numpy in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (1.22.4)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (3.9.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (2.25.1)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (8.4.0)\n",
            "Collecting huggingface-hub>=0.10.0\n",
            "  Downloading huggingface_hub-0.13.2-py3-none-any.whl (199 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m199.2/199.2 KB\u001b[0m \u001b[31m24.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (2022.6.2)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.9/dist-packages (from diffusers==0.10.2) (6.0.0)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.9/dist-packages (from transformers) (6.0)\n",
            "Collecting tokenizers!=0.11.3,<0.14,>=0.11.1\n",
            "  Downloading tokenizers-0.13.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m7.6/7.6 MB\u001b[0m \u001b[31m72.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.9/dist-packages (from transformers) (4.65.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.9/dist-packages (from transformers) (23.0)\n",
            "Requirement already satisfied: wcwidth>=0.2.5 in /usr/local/lib/python3.9/dist-packages (from ftfy) (0.2.6)\n",
            "Requirement already satisfied: torch>=1.4.0 in /usr/local/lib/python3.9/dist-packages (from accelerate) (1.13.1+cu116)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.9/dist-packages (from accelerate) (5.4.8)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.9/dist-packages (from huggingface-hub>=0.10.0->diffusers==0.10.2) (4.5.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/dist-packages (from importlib-metadata->diffusers==0.10.2) (3.15.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->diffusers==0.10.2) (2.10)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.9/dist-packages (from requests->diffusers==0.10.2) (4.0.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->diffusers==0.10.2) (1.26.14)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests->diffusers==0.10.2) (2022.12.7)\n",
            "Installing collected packages: tokenizers, ftfy, huggingface-hub, accelerate, transformers, diffusers\n",
            "Successfully installed accelerate-0.17.0 diffusers-0.10.2 ftfy-6.1.1 huggingface-hub-0.13.2 tokenizers-0.13.2 transformers-4.26.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from flask_ngrok import run_with_ngrok\n",
        "from flask import Flask, render_template, request\n",
        "\n",
        "import torch\n",
        "from diffusers import StableDiffusionPipeline\n",
        "\n",
        "import base64\n",
        "from io import BytesIO\n",
        "\n",
        "# Load model\n",
        "pipe = StableDiffusionPipeline.from_pretrained(\"runwayml/stable-diffusion-v1-5\", revision=\"fp16\", torch_dtype=torch.float16)\n",
        "pipe.to(\"cuda\")\n",
        "\n",
        "# Start flask app and set to ngrok\n",
        "app = Flask(__name__)\n",
        "run_with_ngrok(app)\n",
        "\n",
        "@app.route('/')\n",
        "def initial():\n",
        "  return render_template('index.html')\n",
        "\n",
        "\n",
        "@app.route('/submit-prompt', methods=['POST'])\n",
        "def generate_image():\n",
        "  prompt = request.form['prompt-input']\n",
        "  print(f\"Generating an image of {prompt}\")\n",
        "\n",
        "  image = pipe(prompt).images[0]\n",
        "  print(\"Image generated! Converting image ...\")\n",
        "  \n",
        "  buffered = BytesIO()\n",
        "  image.save(buffered, format=\"PNG\")\n",
        "  img_str = base64.b64encode(buffered.getvalue())\n",
        "  img_str = \"data:image/png;base64,\" + str(img_str)[2:-1]\n",
        "\n",
        "  print(\"Sending image ...\")\n",
        "  return render_template('index.html', generated_image=img_str)\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run()"
      ],
      "metadata": {
        "id": "O3-OhgAqgro1"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}