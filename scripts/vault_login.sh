#!/bin/bash
# Authenticate with Vault using AppRole
RESPONSE=$(curl -k -s --request POST \
  --data "{\"role_id\":\"$VAULT_ROLE_ID\", \"secret_id\":\"$VAULT_SECRET_ID\"}" \
  "$VAULT_ADDR/v1/auth/approle/login")

# Extract client token
VAULT_TOKEN=$(echo $RESPONSE | jq -r '.auth.client_token')

# Get secrets from Vault (e.g. secret/data/flask-app)
SECRETS=$(curl -k -s --header "X-Vault-Token: $VAULT_TOKEN" \
    "$VAULT_ADDR/v1/secret/data/acess_db")

# Extract values
DB_USER=$(echo $SECRETS | jq -r '.data.data.username')
DB_PASS=$(echo $SECRETS | jq -r '.data.data.password')
DB_NAME=$(echo $SECRETS | jq -r '.data.data.database')
DB_HOST=10.0.1.3

# Write to .env file
cat <<EOF > ./app/.env
db_user=$DB_USER
db_password=$DB_PASS
db_name=$DB_NAME
db_host=$DB_HOST
EOF

ls -al ./scripts

echo "[*] Secrets written to .env"

