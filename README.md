# ipm_pest_identifier

The Spanish Ministry of Agriculture created [ 44 official Integrated Pest Management (IPM) guides](https://www.mapa.gob.es/es/agricultura/temas/sanidad-vegetal/productos-fitosanitarios/guias-gestion-plagas) for a wide variety of crops, allowing farmers identify crop pests and diseases.

My goal is to supplement this information with my knowledge as a biologist to create an application that allows users to identify the species present in crops by answering key questions about the current status of the field.

## Methodology

At the beginning, the idea was to automate the whole process by extracting the information directly from the guides using the `pdfplumber` Python library. However, due to the formatting of the PDFs, I decided to manually generate a relational database in `.csv` format to allow the script to extract information accurately.

For the development of this database geared towards Integrated Pest Management (IPM), a structured categorisation based on the trophic guild and the type of damage that the phytophagous arthropod causes to the plant has been used. Under this methodological criterion, the species recorded in the Ministry's guides have been parameterised into standardised agronomic categories (e.g., piercing-sucking, chewing/defoliating, mining, and boring).

This decision responds to two main reasons:
* **Logical Filtering:** Dissociating the type of damage from the affected organ and symptoms allows filtering queries to be executed highly efficiently by exclusion.
* **Scientific Rigour:** Grouping agricultural pests according to their mouthparts and feeding ecology is the standard morphological and functional classification system in plant health literature (Carrero & Planes, 2008; Gabriel-Ortega & Manobanda-Guamán, 2021). Furthermore, understanding these types of damage is the basis for determining the monitoring methods and intervention thresholds (García Marí & Ferragut Pérez, 2002) that form the core of this tool.

The database is divided in four `.csv` for cleaner data management: 
* **`species_data.csv`**: Includes an ID to allow Python to identify the same species across every document (`id`), the crop (`crop`), the scientific name of the species (`scientific_name`) and its common name in Spanish (`spanish_common_name`).
* **`monitoring_data.csv`**: Includes the `id`, the method or methods for monitoring the specie in the field (`monitoring`) how to prevent the overgrowth of the population to avoid a pest situation (`prevention`) and the threshold of intervention if prevention does not work (`threshold`).
* **`control_data.csv`**: Includes the `id`, biological control (biological_control), physics control (Physics_control) and chemical control (Cchemical_control) - the three control methods shown in the guides.
* **`identification_data.csv`**: Includes the `id` and parameters that allow us to identify the species, such as organ of the plant that is damaged (`damage_organ`), the damage that can be seen in the field (`damage_visual`) the category of the damage based on the trophic guild (`damage_cat`) and the period of time (`date`).

### Current database progress
* `species_data.csv`: 3/44
* `monitoring_data.csv`: 3/44
* `control_data.csv`: 3/44
* `identification_data.csv`: 3/44
* **Total: 12/176 (6.82%)**
  
## Crops and areas in the data base
Alfalfa (Alfalfa), Apricot (Albaricoque), Artichoke (alcachofa), Asparagus (Espárrago), Avocado (Aguacate), Banana (Platanera), Beets (Remolacha), Bitter vetch (Yero), Borage (Borraja), Broccoli (Brécol), Brussels sprouts (Col de Bruselas), Cabbage (Repollo), Carob (Algarrobo), Cauliflower (Coliflor), Cherimoya (Chirimoya), Cherry (Cereza), Chestnut (Castaño), Chickpea (Garbanzo), Chinese cabbage (Col China), Citrus (Cítricos), Collard greens (Berza), Conifers (Coníferas), Cotton (Algodón), Cucumber (Pepino), Eggplant (Berenjena), Escarole (Escarola), Eucalyptus (Eucaliptos), Fava bean (Haba), Fenugreek (Alholva), Flat peach (Paraguayo), Flatpod peavine (Titarro), Garlic (Ajo), Grass pea (Almorta), Grasslands (Pastos), Green bean (Judía) , Hardwoods (Frondosas), Hazelnut (Avellano), Hops (Lúpulo), Kiwifruit (Kiwi), Kohlrabi (Colirábano), Leek (Puerro), Lentil (Lenteja), Lettuce (Lechuga), Lupin (Altramuz), Maize (Maiz), Mango (Mango), Melon (Melón), Mushrooms and Fungi (Champiñones y Setas), Narbon vetch (Alverjón), Nectarine (Nectarina), Oaks (Quercus), Olive (Olivar), Onion (Cebolla) , Parks and Gardens (Parques y Jardines), Pea (Guisante), Peach (Melocotón), Pepper (Pimiento), Persimmon (Caqui), Pistachio (Pistacho), Plum (Ciruelo), Pome fruits (Frutales de pepita), Potato (Patata), Pumpkin (Calabaza), Romanesco (Romanesco), Service networks and Industrial areas (Redes de servicio y Zonas industriales), Soybean (Soja), Spinach (Espinaca), Strawberry (Fresa y Fresón), Sunflower (Girasol), Swiss chard (Acelga), Table grapes (Uva de mesa), Thistle (Cardo), Tobacco (Tabaco), Tomato (Tomate), Turnip greens (Grelo), Vetch (Veza), Walnut (Nogal), Watermelon (Sandía), Wine grapes (Uva de transformación), Winter cereals (Cereales de invierno) and Zucchini (Pepino).

## Quick Start & Installation
To run this project locally on your machine, follow these simple steps:
### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.
### 2. Clone the repository
Open your terminal and clone this project:

``` git clone https://github.com/BioPabloCG/ipm_pest_identifier.git```

```cd ipm_pest_identifier```
### 3. Install dependencies
This app requires streamlit and pandas. Install them using pip:

```pip install streamlit pandas```


(Note: If you are using a virtual environment like Anaconda, ensure it is activated before installing).
### 4. Run the application
Launch the Streamlit server by running the following command in your terminal:

```python -m streamlit run ipm_pest_identifier.py```

A new tab will automatically open in your default web browser hosting the local app
## References

### Methodology references
* Carrero, J. M., & Planes, S. (2008). Plagas del campo (13ª ed. rev. y ampl.). Ediciones Mundi-Prensa.
* Gabriel-Ortega, J., & Manobanda-Guamán, M. (Eds.). (2021). Entomología aplicada para Agropecuarios. Grupo COMPAS, Universidad Estatal del Sur de Manabí.
* García Marí, F., & Ferragut Pérez, F. (2002). Las plagas agrícolas. Ediciones Phytoma-España.

### Database references
* [1] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Aguacate. Gobierno de España.
* [2] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Alcachofa y Cardo. Gobierno de España. 
* [3] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Alfalfa. Gobierno de España.
* [4] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Algodón. Gobierno de España.
* [5] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Almendro. Gobierno de España.
* [6] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Arroz. Gobierno de España.
* [7] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Avellano. Gobierno de España.
* [8] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Brassicas: Brécol, Coliflor, Col de Bruselas, Repollo, Col China, Berza, Colirábano, Grelo y Romanesco. Gobierno de España.
* [9] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2022). Guía de gestión integrada de plagas. Caqui. Gobierno de España.
* [10] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2024). Guía de gestión integrada de plagas. Castaño. Gobierno de España.
* [11] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Cereales de invierno. Gobierno de España.
* [12] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Champiñón y Setas. Gobierno de España.
* [13]  Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Chirimoyo. Gobierno de España.
* [14] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2022). Guía de gestión integrada de plagas. Cítricos. Gobierno de España.
* [15] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Coníferas. Gobierno de España.
* [16] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Cucurbitáceas: Calabacín, Calabaza, Melón, Pepino y Sandía. Gobierno de España.
* [17] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Espárragos. Gobierno de España.
* [18] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2018). Guía de gestión integrada de plagas. Eucalipto. Gobierno de España.
* [19] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Fresa y Fresón. Gobierno de España.
* [20] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Frondosas. Gobierno de España.
* [21] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Frutales de hueso: Albaricoque, melocotón, Nectarina, Paraguayo, Ciruelo y Cerezo. Gobierno de España.
* [22] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Frutales de pepita. Gobierno de España.
* [23] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Girasol. Gobierno de España.
* [24] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Hortícolas de hoja: Espinaca, Lechuga, Acelga, Escarola y Borraja. Gobierno de España.
* [25] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Kiwi. Gobierno de España.
* [26] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Leguminosas: Garbanzo, Guisante, Haba, Judía, Lenteja, Soja, Veza y Yero (otras: Alholva, almorta, Altramuz, Alverjón, Algarroba y Titarro. Gobierno de España.
* [27] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Lilíaceas: Ajo, Cebolla y Puerro. Gobierno de España.
* [28] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Lúpulo. Gobierno de España.
* [29] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Maiz. Gobierno de España.
* [30] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Mango. Gobierno de España.
* [31] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Nogal. Gobierno de España.
* [32] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Olivar. Gobierno de España.
* [33] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Parques y Jardines. Gobierno de España.
* [34] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Pastos. Gobierno de España.
* [35] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Patata. Gobierno de España.
* [36] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2024). Guía de gestión integrada de plagas. Pistacho. Gobierno de España.
* [37] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Platanera. Gobierno de España.
* [38] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Quercus. Gobierno de España.
* [39] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Redes de servicio y Zonas industriales. Gobierno de España. 
* [40] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2018). Guía de gestión integrada de plagas. Remolacha. Gobierno de España.
* [41] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Solanáceas: Berenjena, Pimiento y Tomate. Gobierno de España.
* [42] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Tabaco. Gobierno de España.
* [43] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Uva de mesa. Gobierno de España.
* [44] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Uva de transformación. Gobierno de España.



