# ipm_pest_identifier
An automated ETL pipeline and Streamlit web application that digitizes 44 official Integrated Pest Management (IPM) guides from the Spanish Ministry of Agriculture, helping farmers identify crop diseases.

## Methodology
For the development of this database geared towards Integrated Pest Management (IPM), a structured categorisation based on the trophic guild and the type of damage that the phytophagous arthropod causes to the plant has been used. Under this methodological criterion, the species recorded in the Ministry's guides have been parameterised into standardised agronomic categories (e.g., piercing-sucking, chewing/defoliating, mining, and boring).

This decision responds to two main reasons:
- Logical Filtering: Dissociating the type of damage from the affected organ and symptoms allows filtering queries to be executed highly efficiently by exclusion.
- Scientific Rigour: Grouping agricultural pests according to their mouthparts and feeding ecology is the standard morphological and functional classification system in plant health literature (Carrero & Planes, 2008; Gabriel-Ortega & Manobanda-Guamán, 2021). Furthermore, understanding these types of damage is the basis for determining the monitoring methods and intervention thresholds (García Marí & Ferragut Pérez, 2002) that form the core of this tool.

## Crops and areas in the data base
Alfalfa (Alfalfa), Apricot (Albaricoque), Artichoke (alcachofa), Asparagus (Espárrago), Avocado (Aguacate), Banana (Platanera), Beets (Remolacha), Bitter vetch (Yero), Borage (Borraja), Broccoli (Brécol), Brussels sprouts (Col de Bruselas), Cabbage (Repollo), Carob (Algarrobo), Cauliflower (Coliflor), Cherimoya (Chirimoya), Cherry (Cereza), Chestnut (Castaño), Chickpea (Garbanzo), Chinese cabbage (Col China), Citrus (Cítricos), Collard greens (Berza), Conifers (Coníferas), Cotton (Algodón), Cucumber (Pepino), Eggplant (Berenjena), Escarole (Escarola), Eucalyptus (Eucaliptos), Fava bean (Haba), Fenugreek (Alholva), Flat peach (Paraguayo), Flatpod peavine (Titarro), Garlic (Ajo), Grass pea (Almorta), Grasslands (Pastos), Green bean (Judía) , Hardwoods (Frondosas), Hazelnut (Avellano), Hops (Lúpulo), Kiwifruit (Kiwi), Kohlrabi (Colirábano), Leek (Puerro), Lentil (Lenteja), Lettuce (Lechuga), Lupin (Altramuz), Maize (Maiz), Mango (Mango), Melon (Melón), Mushrooms and Fungi (Champiñones y Setas), Narbon vetch (Alverjón), Nectarine (Nectarina), Oaks (Quercus), Olive (Olivar), Onion (Cebolla) , Parks and Gardens (Parques y Jardines), Pea (Guisante), Peach (Melocotón), Pepper (Pimiento), Persimmon (Caqui), Pistachio (Pistacho), Plum (Ciruelo), Pome fruits (Frutales de pepita), Potato (Patata), Pumpkin (Calabaza), Romanesco (Romanesco), Service networks and Industrial areas (Redes de servicio y Zonas industriales), Soybean (Soja), Spinach (Espinaca), Strawberry (Fresa y Fresón), Sunflower (Girasol), Swiss chard (Acelga), Table grapes (Uva de mesa), Thistle (Cardo), Tobacco (Tabaco), Tomato (Tomate), Turnip greens (Grelo), Vetch (Veza), Walnut (Nogal), Watermelon (Sandía), Wine grapes (Uva de transformación), Winter cereals (Cereales de invierno) and Zucchini (Pepino)

## Methodology references
- Carrero, J. M., & Planes, S. (2008). Plagas del campo (13ª ed. rev. y ampl.). Ediciones Mundi-Prensa.
- Gabriel-Ortega, J., & Manobanda-Guamán, M. (Eds.). (2021). Entomología aplicada para Agropecuarios. Grupo COMPAS, Universidad Estatal del Sur de Manabí.
- García Marí, F., & Ferragut Pérez, F. (2002). Las plagas agrícolas. Ediciones Phytoma-España.

## Database references
- [1] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Aguacate. Gobierno de España.
- [2] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Alcachofa y Cardo. Gobierno de España. 
- [3] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Alfalfa. Gobierno de España.
- [4] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Algodón. Gobierno de España.
- [5] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Almendro. Gobierno de España.
- [6] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Arroz. Gobierno de España.
- [7] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Avellano. Gobierno de España.
- [8] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Brassicas: Brécol, Coliflor, Col de Bruselas, Repollo, Col China, Berza, Colirábano, Grelo y Romanesco. Gobierno de España.
- [9] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2022). Guía de gestión integrada de plagas. Caqui. Gobierno de España.
- [10] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2024). Guía de gestión integrada de plagas. Castaño. Gobierno de España.
- [11] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Cereales de invierno. Gobierno de España.
- [12] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Champiñón y Setas. Gobierno de España.
- [13]  Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Chirimoyo. Gobierno de España.
- [14] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2022). Guía de gestión integrada de plagas. Cítricos. Gobierno de España.
- [15] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Coníferas. Gobierno de España.
- [16] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Cucurbitáceas: Calabacín, Calabaza, Melón, Pepino y Sandía. Gobierno de España.
- [17] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Espárragos. Gobierno de España.
- [18] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2018). Guía de gestión integrada de plagas. Eucalipto. Gobierno de España.
- [19] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Fresa y Fresón. Gobierno de España.
- [20] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Frondosas. Gobierno de España.
- [21] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Frutales de hueso: Albaricoque, melocotón, Nectarina, Paraguayo, Ciruelo y Cerezo. Gobierno de España.
- [22] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Frutales de pepita. Gobierno de España.
- [23] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Girasol. Gobierno de España.
- [24] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Hortícolas de hoja: Espinaca, Lechuga, Acelga, Escarola y Borraja. Gobierno de España.
- [25] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Kiwi. Gobierno de España.
- [26] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Leguminosas: Garbanzo, Guisante, Haba, Judía, Lenteja, Soja, Veza y Yero (otras: Alholva, almorta, Altramuz, Alverjón, Algarroba y Titarro. Gobierno de España.
- [27] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2017). Guía de gestión integrada de plagas. Lilíaceas: Ajo, Cebolla y Puerro. Gobierno de España.
- [28] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Lúpulo. Gobierno de España.
- [29] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Maiz. Gobierno de España.
- [30] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Mango. Gobierno de España.
- [31] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2019). Guía de gestión integrada de plagas. Nogal. Gobierno de España.
- [32] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Olivar. Gobierno de España.
- [33] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Parques y Jardines. Gobierno de España.
- [34] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2023). Guía de gestión integrada de plagas. Pastos. Gobierno de España.
- [35] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Patata. Gobierno de España.
- [36] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2024). Guía de gestión integrada de plagas. Pistacho. Gobierno de España.
- [37] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Platanera. Gobierno de España.
- [38] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2016). Guía de gestión integrada de plagas. Quercus. Gobierno de España.
- [39] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2020). Guía de gestión integrada de plagas. Redes de servicio y Zonas industriales. Gobierno de España. 
- [40] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2018). Guía de gestión integrada de plagas. Remolacha. Gobierno de España.
- [41] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2021). Guía de gestión integrada de plagas. Solanáceas: Berenjena, Pimiento y Tomate. Gobierno de España.
- [42] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2015). Guía de gestión integrada de plagas. Tabaco. Gobierno de España.
- [43] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Uva de mesa. Gobierno de España.
- [44] Ministerio de Agricultura, Alimentación y Medio Ambiente. (2014). Guía de gestión integrada de plagas. Uva de transformación. Gobierno de España.



