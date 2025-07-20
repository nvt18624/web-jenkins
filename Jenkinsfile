pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
  }

  stages {
    stage('Vault Login & Generate .env') {
      steps {
        sh '''
          echo "[INFO] Logging into Vault and generating .env file..."
          chmod +x ./scripts/vault_login.sh
          ./scripts/vault_login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
          ls -al ./
          ls -al ./app/
        '''
        stash includes: 'app/.env', name: 'env-file'
      }
    }

  stage('Ansible Deploy') {
    steps {
      unstash 'env-file'

      withCredentials([
        sshUserPrivateKey(credentialsId: 'GG_CLOUD_PRIVATE', keyFileVariable: 'KEY_FILE')
      ]) {
        sh '''
          echo "[INFO] Using SSH key at $KEY_FILE"
          chmod 600 "$KEY_FILE"
          cd ansible
          ansible-playbook ./playbooks/deploy.yml \
            -i ./inventories/webs.ini 
        '''
        }
      }
    }
  }
}

