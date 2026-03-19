import streamlit as st
import pandas as pd

#Site configuration
st.set_page_config(page_title="Identificador de plagas", layout="wide")
st.title("🌱 Identificador de plagas en cultivos agrícolas")

#Function to load and merge data from the 4 .csv files
@st.cache_data
def load_data():
    df_species = pd.read_csv("species_data.csv", sep=";", dtype={"id": str})
    df_ident = pd.read_csv("identification_data.csv", sep=";", dtype={"id": str})
    df_monit = pd.read_csv("monitoring_data.csv", sep=";", dtype={"id": str})
    df_control = pd.read_csv("control_data.csv", sep=";", dtype={"id": str})
    
    #Merging tables using 'id' as the primary key
    df_merged = df_species.merge(df_ident, on="id", how="left")
    df_merged = df_merged.merge(df_monit, on="id", how="left")
    df_merged = df_merged.merge(df_control, on="id", how="left")
    
    #Handling missing values
    df_merged = df_merged.fillna("Información no disponible")
    return df_merged

try:
    df = load_data()
except Exception as e:
    st.error(f"⚠️ Error al cargar los archivos. Detalle: {e}")
    st.stop()

#Sidebar visual diagnostic system
st.sidebar.header("🔍 Diagnóstico de campo")
st.sidebar.markdown("¿Qué se observa en la parcela?")

#Filter 1: Crop
crops = df['crop'].unique().tolist()
crop_selected = st.sidebar.selectbox("Selecciona tu cultivo:", crops)

df_filtered = df[df['crop'] == crop_selected]

#Filter 2: Affected organ (Multiselect with clean options)
organ_dictionary = {
    "Hoja (General)": "hoja",
    "Hoja (Envés)": "envés",
    "Hoja (Haz)": "haz",
    "Ramas": "rama|brote",
    "Fruto": "fruto",
    "Tronco": "tronco|cuello|madera",
    "Tallos": "tallo",
    "Tubérculos": "tubérculo|tuberculo|patata",
    "Brote": "brote|tierno",
    "Raíces": "raíz|raíc|raic|radicular",
    "Copa del árbol": "copa",
    "Suelo": "suelo|tierra",
    "Planta completa": "general|planta|completo"
}

organ_selected = st.sidebar.multiselect(
    "¿Qué parte(s) del árbol está(n) afectada(s)?", 
    list(organ_dictionary.keys()),
    placeholder="Elige una o varias opciones..."
)

#Filter applied only if the user has selected at least one organ
if organ_selected:
    #Join expressions of the selected organs (OR logic)
    organ_pattern = "|".join([organ_dictionary[org] for org in organ_selected])
    #Looking for matches in both the 'damage_organ' and 'damage_visual' columns for better accuracy
    df_filtered = df_filtered[
        df_filtered['damage_organ'].str.contains(organ_pattern, case=False, na=False, regex=True) |
        df_filtered['damage_visual'].str.contains(organ_pattern, case=False, na=False, regex=True)
    ]

#Filter 3: Visual symptoms (Expanded dictionary with comprehensive keywords)
symptoms_dictionary = {
    "Cualquier síntoma": "",
    "Manchas / Necrosis / Costras": "mancha|necrót|necrosis|costrosa|chancro",
    "Defoliación / Caída de hojas o frutos": "defoliación|caen|caída",
    "Decoloración / Amarilleamiento / Clorosis": "decoloración|amarill|bronceado|platead|cloróti|ceniciento",
    "Marchitez / Decaimiento / Seca regresiva": "marchit|debilitamiento|decaimiento|muerte|seco|seca|regresiva", # "marchit" capta marchitez y marchitamiento
    "Melaza / Negrilla / Secreciones": "melaza|negrilla|hollín|secreción|secrecion",
    "Cicatrices / Grietas / Deformaciones": "cicatrices|deform|raspaduras|corchoso|agrietadas|resquebrajarse",
    "Podredumbre / Pudrición": "podredumbre|pudrición",
    "Perforaciones / Galerías / Roeduras (Planta)": "galería|galeria|perforaciones|agujero|serrín|roeduras|punteaduras|incisiones|orificios",
    "Seda / Nidos / Telarañas": "seda|nido|telaraña",
    "Presencia de Hormigas": "hormiga|hormiguero",
    "Insectos / Larvas / Masas algodonosas": "algodono|caparazon|colonias|ninfa|adulto|larva|insecto|gusano|oruga|blanca", # Añadido larva, insecto, gusano y blanca
    "Exudados (Líquidos oscuros en tronco/raíz)": "exudado",
    "Indicios de Vertebrados en el suelo": "topera|huella|excremento|hozadura|bano|baño|cama|madriguera|hura", # NUEVO: Para jabalíes, ratas topo, topillos, etc.
    "Síntomas generales de enfermedad": "síntoma|sintoma|daño|dano|infección|infeccion" # NUEVO: Para hongos y virus genéricos
}

symptoms_selected = st.sidebar.selectbox("¿Cuál es el síntoma principal?", list(symptoms_dictionary.keys()))

if symptoms_selected != "Cualquier síntoma":
    keyword = symptoms_dictionary[symptoms_selected]
    df_filtered = df_filtered[df_filtered['damage_visual'].str.contains(keyword, case=False, na=False, regex=True)]

#Diagnosis results
st.write(f"### 🔎 Resultados: {len(df_filtered)} posible(s) especie(s) detectada(s)")

if len(df_filtered) == 0:
    st.warning("No hemos encontrado ningún problema que coincida exactamente con esos filtros. Prueba a quitar alguna parte afectada o marca 'Cualquier síntoma'.")
else:
    st.markdown("Selecciona una de las posibles causas para ver su ficha y confirmar si coincide con tus daños:")
    pest_list = df_filtered['spanish_common_name'] + " (" + df_filtered['scientific_name'] + ")"
    pest_selected = st.selectbox("Posibles causantes:", pest_list.tolist())
    
    #Display detailed information for the selected pest
    if pest_selected:
        pest_data = df_filtered[df_filtered['spanish_common_name'] + " (" + df_filtered['scientific_name'] + ")" == pest_selected].iloc[0]
        
        st.header(f"🐛 {pest_data['spanish_common_name']}")
        st.subheader(f"*{pest_data['scientific_name']}*")
        
        tab1, tab2, tab3 = st.tabs(["🔎 Identificación y daños", "📊 Monitoreo y prevención", "🛡️ Control y tratamiento"])
        
        with tab1:
            st.write("### Identificación visual")
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Órgano afectado:** {pest_data['damage_organ']}")
            with col2:
                st.warning(f"**Época de riesgo:** {pest_data['date']}")
            
            st.write("**Daños visuales en el campo:**")
            st.success(pest_data['damage_visual'])
            st.caption(f"Clasificación técnica del daño: {pest_data['damage_cat']}")
            
        with tab2:
            st.write("### Estrategia de monitoreo")
            st.write("**Método de seguimiento:**")
            st.info(pest_data['monitoring'])
            
            st.write("**Medidas de prevención:**")
            st.success(pest_data['prevention'])
            
            st.write("**Umbral de intervención:**")
            st.error(pest_data['threshold'])
            
        with tab3:
            st.write("### Métodos de Control")
            st.write("**🔵 Control biológico/biotecnológico:**")
            st.info(pest_data['biological_control'])
            
            st.write("**🟡 Control físico:**")
            st.warning(pest_data['physical_control'])
            
            st.write("**🔴 Control químico:**")
            st.error(pest_data['chemical_control'])

#Authorship
st.sidebar.markdown("---") 
st.sidebar.markdown("### 👨‍💻 Sobre el proyecto")

st.sidebar.info(
    "Este proyecto personal realizado de forma autónoma se ha desarrollado para profundizar "
    "en mi formación y enlazar la bioinformática y la ecología. Es posible que existan "
    "errores de código o taxonomía, ante cualquier sugerencia o comentario no duden en contactar conmigo."
)

#Links to professional profiles
st.sidebar.markdown("🌐 [Mi perfil de GitHub](https://github.com/BioPabloCG)")

st.sidebar.markdown("💼 [Conecta en LinkedIn](https://www.linkedin.com/in/pablo-c-637a1816a/)")
