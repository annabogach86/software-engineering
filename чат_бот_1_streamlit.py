{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMXefdKLihDn5hSnJb3hzH3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/annabogach86/software-engineering/blob/main/%D1%87%D0%B0%D1%82_%D0%B1%D0%BE%D1%82_1_streamlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2DAtaGrQ35lL"
      },
      "outputs": [],
      "source": [
        "pip install streamlit transformers"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from transformers import pipeline"
      ],
      "metadata": {
        "id": "z0KIV5dj6-CJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Загрузка модели DistilBERT\n",
        "model = pipeline(\"question-answering\", model=\"distilbert-base-uncased-distilled-squad\")"
      ],
      "metadata": {
        "id": "jkAm_wCz7KaD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Заголовок приложения\n",
        "st.title(\"Чат-бот на основе DistilBERT\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hZCryCkP7R87",
        "outputId": "727dfb2b-6a27-4855-b685-06e10ce0edc9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Контекст пользователя\n",
        "context_input = st.text_input(\"Введите контекст: \")\n",
        "# Вопрос пользователя\n",
        "user_input = st.text_input(\"Введите вопрос: \")"
      ],
      "metadata": {
        "id": "qQQXb7Xi75XX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Ответ бота\n",
        "if user_input:\n",
        "    # Получение ответа от модели\n",
        "    answer = model({\n",
        "        \"question\": user_input,\n",
        "        \"context\": context_input\n",
        "    })\n",
        "\n",
        "    # Вывод ответа\n",
        "    st.write(\"Ответ:\", answer[\"answer\"])"
      ],
      "metadata": {
        "id": "w6pN8AYd7YfP"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}