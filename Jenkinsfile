pipeline {
    agent any
    stages {
        stage('Init Vault Credentials') {
            steps {
                withCredentials([
                    string(credentialsId: 'VAULT_ADDR', variable: 'VAULT_ADDR'),
                    string(credentialsId: 'VAULT_ROLE_ID', variable: 'VAULT_ROLE_ID'),
                    string(credentialsId: 'VAULT_SECRET_ID', variable: 'VAULT_SECRET_ID')
                ]) {
                    sh '''
                        echo "VAULT_ADDR=$VAULT_ADDR"
                        echo "ROLE_ID=$VAULT_ROLE_ID"
                        echo "SECRET_ID=$VAULT_SECRET_ID"
                        bash ./scripts/vault_login.sh
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building app..."
            }
        }
    }
}

