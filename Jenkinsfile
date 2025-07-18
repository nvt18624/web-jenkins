pipeline {
    agent {
        docker {
            image 'tingy01052004/iac:v1.0.2'
            args '-u root'
            reuseNode true
        }
    }

    stages {
        stage('Init Vault Credentials') {
            steps {
                withCredentials([
                    string(credentialsId: 'VAULT_ADDR', variable: 'VAULT_ADDR'),
                    string(credentialsId: 'VAULT_ROLE_ID', variable: 'VAULT_ROLE_ID'),
                    string(credentialsId: 'VAULT_SECRET_ID', variable: 'VAULT_SECRET_ID')
                ]) {
                    sh '''
                        export VAULT_ADDR=$VAULT_ADDR
                        export ROLE_ID=$VAULT_ROLE_ID
                        export SECRET_ID=$VAULT_SECRET_ID
                        chmod +x ./scripts/vault_login.sh
                        ./scripts/vault_login.sh
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building app..."
                // build commands here
            }
        }
    }
}

