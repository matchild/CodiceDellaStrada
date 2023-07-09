# CodiceDellaStrada
An AI question-answering system trained on Italian traffic laws. This project aims to develop a system where the user can query the Italian traffic code using natural language and receive precise and reliable answers. 

## Install

```bash
git clone https://github.com/matchild/CodiceDellaStrada.git
pip install -r requirements.txt
```

## Sample usage
Just run the main.py file and ask your questions. On linux this can be done with:
```bash
python3 main.py
```
## Examples

**Query**: What is the fine in case of speeding?

**Answer**: _It depends on how much the speed limit is exceeded. If the speed limit is exceeded by up to 10 km/h, the fine is between €39 and €159. If the speed limit is exceeded by between 10 km/h and 40 km/h, the fine is between €159 and €639. If the speed limit is exceeded by between 40 km/h and 60 km/h, the fine is between €500 and €2,000. If the speed limit is exceeded by more than 60 km/h, the fine is between €779 and €3,119._

---

**Query**: In which situations it is allowed to not wear a seatbelt?

**Answer**: _According to Article 172 of the Italian driving code, it is allowed to not wear a seatbelt in the following situations: for members of the police force and municipal police carrying out an emergency service, for drivers and attendants of fire and ambulance services in case of emergency, for children under three years old travelling in vehicles with front airbags unless the airbag has been deactivated, and for children under 1.5 meters tall travelling in public service vehicles or vehicles for hire with a driver, provided they are accompanied by a passenger aged 16 or over._

---

**Query**: What is the speed limit in urban areas?

**Answer**: _50 km/h_

## How does it work?
The _/knowledge_ folder contains a database of embeddings obtained from recursively applying an embedding function (_Ada v2_) to all articles of the regulation[^1]. When a query is run, the algorithm embeds the question with the same function used to create the database, returns the most similar vectors, and provides the corresponding text chunks to the language model as context.

[^1]:More precisely to 1000 character long chuncks of the original document.

## Disclaimer

This work is to be intended for research purposes only and there is no guarantee that the answers are always 100% accurate. For more details on Italian traffic regulations refer to the official [Codice della Strada](https://www.gazzettaufficiale.it/dettaglio/codici/strada).

## Requirements
The project is based on the following libraries: `tiktoken unstructured chromadb openai langchain`

## Credits

A big thank you to the Italian police IT team for providing a clean pdf version of the regulation.
This work is based on the amazing [langchain](https://github.com/hwchase17/langchain) library that allows to formulate complex queries to llms while interacting with local databases.

