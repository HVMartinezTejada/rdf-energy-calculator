import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA
# ==============================================================================
st.set_page_config(page_title="PCI Calculator Pro", layout="wide")

# ==============================================================================
# LOGO E IDENTIDAD
# ==============================================================================
logo_base64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAACWUExURUxpcY7GR47GR47GR47GR47GR47GR47GR47GR47GR47GR47GR47GR47GR47GR47GRzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUlzFUl1uIc1qHc47GRzFUl4i/TDdbklR/eWubZUhxgz1ijUJpiH2xVneqW4K4UU54fnGiYGWUamCNb1qGdOUPuYwAAAAhdFJOUwCAMCBAYJ/vvxDP33CPr1AQ74BAIL/Pr59gcFCPMN+vjzfN+/kAAAjhSURBVHja7Z3Xeqs4EIAlLEB0O3acnl1w3BKnvf/L7YXjmKIBSYzA2i9zfczhz/RRgZA/+ZM/GVkcdpLAxtefsJimPMzrwrlHYzaxQwVuwvMu4R69aA05cern0hJ5sXOBEIHrKUCcxE/dyWVRpLm2hMmlKIbp6KJqZcn4egniKMeQ0B3V+ye9lVESbzQTc7wcV7g7CgbP8SVyhzeq3IwMixIkuTkZEMX1c6PC2TDOEebGxQvstqpS8RKbTuM98l/IOT1KwiVKZKPZXksdnFPKWLPg96KxlCLlHa+br/X2KP9QxsTp2smox6OxlNIdrD6+t8VJbu6m4gyUJdKp1M9MeHlHClxt3n8hiqWYIsg8RR9L8FN5KE0xe1yIG0iduB0im5fTZlZv65czxvWd8PeJbrjzUYtit00ZuzNFcfuESpHneZ4jliwx+J8cvkvKmF0JbGoS964E0BwFdPPDuihjNB08S1AaSM8sRxdGQNGKyzAwx1HBKETawKyREUjEHKsKxo3IN3Br/d4kYo6vkosXz3PFQDcGiZDjY1dxDtVINwaJiOPwXraq6wVUCqD3KClu/vgsW9XsHv5xivDu0W8LQ1OeYubzw7asjuVTW5XZKxFyD28lxelQR/HYUS9r6gR7waEZP1cV75g9dJumrw6BvtDQtIzXnbRZyTYxtdWS2ERL2HiFz6ISraa404owMTTMcltTeXGr8CQuYU/G5lj1Ruqwr3BcqXlbSw3sp2aXEmsO8lqJVsWdxkIpbzo+T1zTayK1+dWmL8dRMYxSj3POOafUHWS9ndU4CgyOMRYGo/8HR82w1tZyOG0ct/ZwEP4/4XBbOJZTezgCH/bzmUUcFU+vcRRPFnGUO9SPGse9RRzlordWlxQ3NnGUQu/hxWIHKYXe1b5mWHObOBgYeLsa9AuTFOgHbTOsc8h6q3EUD8TKkLWqOXpxTexUyLaukIVVIBRyEMUe/WKqrNfCak8/l717uxXyOzn5slwhDmRYtinEgwzLMoUQH4hYlhUnJ1ev17zW5ZBTmbVucNzYxREANZZtVdbJshqeXjwTGy1rU9ju6uRY9O6aIE92cWTinG6fZSXCLsRCywoBhdg1cvgJviKFFMRCFxEpxLJseOwNRQqxrPAlXJxDrHMREuV5/l7Y7yIkz/OViGNpGYcDWdatZSAMsqwr+0CElmWdr9Pm6pSVFSOhos7QcNAKfm61mCCD7EQcM2wTZjFNuPBai5RS5iCAvAoVco32148plzlZFaX9rrWggiEQEkiQUe4PtkEzbq4jYJSMgevpHh+JEq0Db0wcfHulkd4neXxPnYVtkEEQziNp3WoRbLFB0M7tczW1FOimNUG7SSFS2UuLD0JIFmGh+DQYE0RtP3kHijsmCOp5sUjKV6aGQDpO+Cq6vUQEm5sC0T5DomlfxjRCWo6VGjkhCoCgTLUwj791nnwDQHCqX3dAEqMgQ5IAIFiN1XDWBYCgtbqSHh/K3NfFdUAWw5JkhGTd/7LtnP4MAMEbB8llxiQgJHDDbl5IrgEQvDMWgVwJebwJpeMuNT9QBkGcNDqSdVc66W5o4MR4azb+HitItYucWlHAM4tXAAjqmi5VLA9bejMwct2bjr+/y0lKt2vBvRlTLH9xp9iBfM/Ij/4MXkvGFctf5JMWjkLN/vM3Z76aSqBEgrzSo1Kr0B81cqXABcVf7LU3lT7rdKMeVcklV4N4u5KbnOtD4Q1lQLv4MIi3K+TFConoR96o3q7anLSQ+MDzl8N4u2oT30ICLAs9DpHbj24S4pCoOgn+Zlm165E8yLkSRScxcFo6UwE55ZP6IXswud+YHAnplo+VPqoWJkLVutHEznilNQd/Ig4TwLMXA9qWWl48G1EoAwIGYCM7hJTyYh4Lw4RyT2JkQ4qrZVyZDAgYt8wc3VO6cTcVFZ3go28GVYmaw5/aj/K1AeCTwZxoZh+dUoYPBR0N/OjnwvxUSNfh3UbkiuAng02JoX1bCp3v+bWZxAwYTCWmNmm6OipJJUbAtyDJv6OT/CpgUksuSlOhYhM6Ywdhp9bQtL4QNIMovpFvQtZos7yqSnytdepin49Ocp6bcIl7NEGVHMYncSuBq2PRHVTJZ57nkZkr72LVOoVErWsk7SrZdS7fmY9dQekHnXsHQJW8ldtOZGG+mm0Fft5t5lDpuM0lLFN7HhEqxS3iSdjGolUlvqn7CBOVMoUwmWs2H1tVYoxE5q5QtWAzhZYYPsySSHxrRvG6U6gv2a0qSzAGPIXLerukXIN1Sm7S4wkhjEvN6mRlMWvz947Cs69W2rajKEf/+3bjQvvYATBRBVnU01iXceF87KCld4y9EAWk07gMuvw5jDGWJT1BwMj1surz1K43jznntS9vcsltQcpp8V1tI67SjP7HNfj5HEwQyyxStQs0Ct40d1rgZ3af8yTljaNAWg+G3OTltTw3w0rzUvvoNbsIqKDfr+p73hB6K6k6XtcAoGyy1j0TATZWkqsl2j5529L2Vk6q9Mt/oXKri5YXP+qNgr5WXPm1qx6Za7qUcPijgWl9rHhCI41RIybJbiX4j1S/K5CpHcnoV0pAQXi/Ep8clGbJVD+S3PfzYk8zcPQo9kiJTyVM3FT5zFL/KhUiWcOzzZaTwwGLU53TcBgNtjrJscjwqHs+rT5hzKUJ1z48htKULpY6JKiC1FxPxyZBGxJMgcy4XtnFAVcr+wFIfNyhzd1YJOgDwflMslrBFQNTDiB4vXyY5MD/rm5LH/9lzqwyYkYexOb1bshRDH4QfCpeBtqZcBTDn2gHlPJpkzpalYJsXobV8ROIn41HLy8gg8jVzKhSOCNDyVRYsrxsMDAilwwpCyHK9mAZBozytbIM44gyQ7WvcBwMQgiZXgki2O5NL1IxMqo8CPLKVhkljAMyukzvl/1QosQhFyKLJstWMkGGl0Pxo5e7uo3tOt3ex/8cMI5e6iz7lqo4vFCIX99/XHY1XRGnLiM2yPz+8foUlnffH0e/55ynQ328FdnQ5vP5/OF+Pp/Pn8if/ImN8h9yNdvG0ZIiQQAAAABJRU5ErkJggg"
# Encabezado con logo y fondo blanco

st.markdown(f"""
<div style="background: white; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <img src="{logo_base64}" width="80" style="margin-bottom: 10px;">
    <h2 style='color: #2E86C1; margin: 0; border-bottom: 2px solid #3498DB; padding-bottom: 5px; font-size: 5vw;'>
        PCI y Emisiones No Causadas
    </h2>
    <p style='color: #7B8A8B; font-size: 2vw; margin: 5px 0 0;'>
        Creado por: HV. Martínez-Tejada | GeoFuturo CDR
    </p>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# PARÁMETROS CIENTÍFICOS
# ==============================================================================
FACTOR_DESPLAZAMIENTO = 1.20   # t-CO₂eq/ton-RS
FACTOR_DISPOSICION = 1.95      # t-CO₂eq/ton-RS
FE_TOTAL = FACTOR_DESPLAZAMIENTO + FACTOR_DISPOSICION
KG_CO2_POR_ARBOL_ANUAL = 22
ANOS_ABSORCION = 20

# ==============================================================================
# BASE DE DATOS ACTUALIZADA
# ==============================================================================
@st.cache_data

def load_data():
    return pd.DataFrame({
        "ID": list(range(1, 35)),
        "Familia": [
            "Orgánico", "Orgánico", "Orgánico", "Orgánico", "Orgánico", "Orgánico", "Mixto", "Inorgánico", "Mixto", "Orgánico", "Inorgánico",
            "Biomasa", "Biomasa", "Biomasa", "Biomasa", "Biomasa", "Biomasa", "Biomasa", "Biomasa",
            "Caucho", "Caucho", "Caucho",
            "EPP",
            "Plástico", "Plástico", "Plástico", "Plástico", "Plástico",
            "Poliestireno", "Poliuretano", "Textiles", "Polímeros",
            "Mixto", "Tóner"
        ],
        "Material": [
            "Virutas de madera", "Serrín", "Cáscara de arroz", "Bagazo", "Residuos de alimentos", "Estiércol", "Residuos sólidos urbanos",
            "Residuos plásticos", "Neumáticos usados", "Residuos de papel", "Escombros",
            "Arroz Quemado", "Aserrín", "Cartón Plegadiza", "Cascarilla Arroz", "Madera No aprovechable",
            "Materia vegetal no aprovechable", "Trigo no conforme", "Harina no conforme",
            "Globos de Latex", "Latex", "Sólidos contaminados con latex",
            "EPP y Dotaciones",
            "Bigbags", "Bolsas Scholle", "Estibas plásticas", "Residuos Cinta adhesiva con celulosa", "Plástico no aprovechable",
            "ICOPOR", "Poliuretano", "Marquilla", "Silicona",
            "Materiales mixtos (celulosa/plástico)", "Tóner con tinas no peligrosas"
        ],
        "PCI (kcal/kg)": [
            4000, 4200, 3000, 3300, 1700, 1300, 2200, 10000, 10000, 3700, 0,
            3770, 3900, 3400, 3700, 3000, 1500, 3780, 3950,
            10000, 10000, 3200,
            4300,
            11000, 8000, 10000, 5000, 8000,
            10030, 6800, 4300, 5570,
            6000, 8000
        ],
        "Humedad (%)": [
            12, 10, 8, 12, 70, 65, 30, 5, 2, 8, 5,
            12, 10, 5, 0, 20, 60, 13, 12,
            0, 0, 0,
            4,
            0, 0, 0, 0, 0,
            0, 3, 0, 0,
            4.5, 2.7
        ]
    })

df = load_data()

# ==============================================================================
# INTERFAZ DE USUARIO
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Parámetros de Entrada")
    n = st.slider("Número de corrientes de residuos:", min_value=1, max_value=len(df), value=1)
    st.markdown("---")
    st.info("ℹ️ Seleccione el material y su cantidad en kg")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📚 Base de Materiales")
    st.dataframe(
        df[['ID', 'Familia', 'Material', 'PCI (kcal/kg)', 'Humedad (%)']],
        height=500,
        use_container_width=True,
        hide_index=True
    )

with col2:
    st.subheader("🧮 Formulación de Mezcla")
    inputs = []
    cols = st.columns(2)

    for i in range(n):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"#### 🧪 Material {i+1}")
                residuo_id = st.selectbox(
                    f"ID del material {i+1}",
                    options=df['ID'],
                    key=f"id_{i}",
                    format_func=lambda x: f"{x} - {df.loc[df['ID'] == x, 'Material'].values[0]}"
                )
                cantidad = st.number_input(
                    f"Cantidad (kg) {i+1}",
                    min_value=0.0,
                    value=0.0,
                    key=f"cant_{i}",
                    step=0.5
                )
                inputs.append((residuo_id, cantidad))

# ==============================================================================
# CÁLCULOS Y RESULTADOS
# ==============================================================================
if st.button("⚡ Calcular PCI", type="primary", use_container_width=True):
    total_weight = sum(cantidad for (_, cantidad) in inputs)
    if total_weight <= 0:
        st.error("❌ Error: La masa total debe ser mayor que 0 kg")
    else:
        contributions = []
        for residuo_id, cantidad in inputs:
            pci = df.loc[df['ID'] == residuo_id, 'PCI (kcal/kg)'].values[0]
            contributions.append(cantidad * pci)

        mixture_PCI = np.sum(contributions) / total_weight

        st.success("✅ Cálculo completado")

        tab1, tab2, tab3 = st.tabs(["📊 Resultados", "📈 Gráfica", "🌱 Sustentabilidad"])

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Masa Total", f"{total_weight:,.2f} kg")
                st.metric("PCI de Mezcla", f"{mixture_PCI:,.2f} kcal/kg")
            with col2:
                st.metric("Estado CDR", "🟢 Apto" if mixture_PCI > 4500 else "🔴 No Apto")

        with tab2:
            fig = px.pie(
                names=[df.loc[df['ID'] == id, 'Material'].values[0] for id, _ in inputs],
                values=[w for _, w in inputs],
                hole=0.3,
                color_discrete_sequence=px.colors.sequential.Blues_r
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            if mixture_PCI > 4500:
                co2_evitado = (total_weight / 1000) * FE_TOTAL
                arboles = int((co2_evitado * 1000) / (KG_CO2_POR_ARBOL_ANUAL * ANOS_ABSORCION))
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("CO₂ evitado", f"{co2_evitado:,.1f} ton")
                with col2:
                    st.metric("Equivalente en árboles", f"{arboles} árboles")

                st.markdown("""
                | Componente               | Valor (t-CO₂eq/ton-RS) |
                |--------------------------|-------------------------|
                | Desplazamiento de carbón | 1.20                    |
                | Disposición evitada RS   | 1.95                    |
                | **Total**                | **3.15**                |
                """)

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D;">
    <p>© 2025 GeoFuturo CDR | 
    <a href="#" style="color: #2980B9; text-decoration: none;">Políticas de Privacidad</a> | 
    <a href="#" style="color: #2980B9; text-decoration: none;">Soporte Técnico</a></p>
</div>
""", unsafe_allow_html=True)
