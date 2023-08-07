# News Summary Generator

The News Summary Generator is a Python application that generates a summary of a news article using Llama-7b. This application fetches the article from a URL provided by the user, extracts the article's content, and sends it to the Monster API to generate the summary.

## Installation

Before you can run the script, make sure you have Python installed on your machine. You also need to install a couple of Python libraries which the script depends on. You can install them using pip:

```bash
pip install requests newspaper3k
```

## Configuration

In order to use this script, you'll need to get an API key and an Authorization token from the [MonsterAPI](https://monsterapi.ai/). Replace `YOUR_MONSTER_API_KEY` and `YOUR_MONSTER_AUTH_TOKEN` in the script with your actual API key and auth token.

## Usage

To use the News Summary Generator, run the script and input the URL of the news article when prompted:

```bash
python news_summary_generator.py
Enter the URL of the article: <Paste your URL here>
```

```Example Input/Output
Enter the URL of the article: https://www.philschmid.de/sagemaker-llama-llm
 The article discusses how to deploy the LLaMA model, which is a next-generation language model trained on more data and with improved capabilities compared to its predecessor. To deploy this model on Amazon SageMaker, you will use the Hugging Face Large Language Model (LLM) Docker Container (DLC), which provides a secure and managed environment for deploying and serving large language models.
To begin, you need to set up your development environment by installing the AWS SDK and configuring an IAM role with the required permissions for Sagemaker. Once you have completed these steps, you can retrieve the new Hugging Face LLM DLC using the `sagemaker .get_execution_role()` method or by retrieving it directly from the AWS API.
Once you have retrieved the container URI, you can provide it to the `HuggingFaceModel` class along with an image URI pointing to the image containing the LLaMA model. This will allow you to deploy the model in a scalable and optimized manner.
The article also includes hardware requirements for different model sizes, which are important to consider when deploying the model to ensure optimal performance. Overall, the process of deploying the LLaMA model on Amazon SageMaker involves using the Hugging Face LLM DLC and configuring the necessary dependencies and roles to enable seamless deployment and management of the model.
```

The script will fetch the article, extract the content, and send it to the Monster API. It will then print out the summary of the article, or an error message if something went wrong.

## Limitations

The News Summary Generator uses the newspaper3k library to extract article content, which may not work perfectly for all webpages due to the variability in website designs.

The script currently uses the first 2048 characters of the article content for the summary due to the input length limit of the Monster API. Future enhancements will break the text into chunks, send them to the model separately, and then combine the summaries.

## Contributing

Contributions are welcome. Please open an issue to discuss the changes, or open a pull request with changes.

## License

The News Summary Generator is open-source software licensed under the MIT license.
