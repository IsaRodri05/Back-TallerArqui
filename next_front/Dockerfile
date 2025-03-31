# Etapa 1: Construcción de la aplicación
FROM node:20-alpine AS builder

WORKDIR /app

# Copiar package.json y lockfile primero para aprovechar la cache de Docker
COPY package.json package-lock.json* ./

# Instalar solo dependencias necesarias para construir
RUN npm install --frozen-lockfile

# Copiar el resto del código fuente
COPY . .

# Construir la aplicación
RUN npm run build

# Etapa 2: Imagen final optimizada
FROM node:20-alpine

WORKDIR /app

# Copiar archivos necesarios desde la etapa de construcción
COPY --from=builder /app/package.json /app/package-lock.json ./
COPY --from=builder /app/.next .next
COPY --from=builder /app/public public
COPY --from=builder /app/node_modules node_modules

# Exponer el puerto
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]
