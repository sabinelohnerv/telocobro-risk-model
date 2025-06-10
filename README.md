
# 📊 API de Riesgo de Morosidad

Esta API predice si un cliente tiene alto riesgo de impago, utilizando un modelo de árbol de decisión entrenado previamente. Está construida con **FastAPI**, es modular, y utiliza autenticación mediante **API Key**.

---

## 🚀 Características

- 🔐 Autenticación por API Key
- 📈 Predicción de riesgo de morosidad a partir de 5 variables
- 📦 Carga automática del modelo `.pkl`
- ⚙️ API REST compatible con Swagger UI

---

## 🧠 Requisitos del modelo

El modelo fue entrenado con las siguientes características:

- `totalDebtBOB` (float)
- `totalPendingDebtBOB` (float)
- `averagePaymentTime` (float)
- `paymentDelayRate` (float)
- `debtCount` (int)

---

## 📁 Estructura del proyecto

```
risk_model_api/
├── main.py
├── .env
├── requirements.txt
├── saved_model/
│   └── model.pkl
├── routers/
│   └── predict.py
├── models/
│   └── schemas.py
├── services/
│   └── model_service.py
├── utils/
│   └── security.py
```

---

## 🛠️ Instalación y ejecución

1. Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/risk_model_api.git
cd risk_model_api
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Crea el archivo `.env` con tu clave de API:
```ini
API_KEY=tu_api_key_secreta
```

5. Coloca tu modelo entrenado en `saved_model/model.pkl`.

6. Ejecuta el servidor:
```bash
uvicorn main:app --reload
```

---

## 🧪 Cómo probar

### Swagger UI
Abre en tu navegador:

```
http://localhost:8000/docs
```

Presiona **Authorize** e ingresa tu API Key como:

```
x-api-key: tu_api_key_secreta
```

### Ejemplo de JSON para `/predict`:

```json
{
  "totalDebtBOB": 12000,
  "totalPendingDebtBOB": 5000,
  "averagePaymentTime": 18.7,
  "paymentDelayRate": 0.33,
  "debtCount": 7
}
```

### Respuesta esperada:

```json
{
  "prediction": 1,
  "probability": 0.65,
  "threshold": 0.4
}
```

---

## 📦 Variables de entorno

- `API_KEY`: Clave secreta para proteger la API.

---

## 🔐 Seguridad

Esta API implementa autenticación por **API Key** mediante el header `x-api-key`. No se permite el acceso sin clave válida.
