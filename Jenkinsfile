pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
    PRIVATE_KEY     = credentials('GG_CLOUD_PRIVATE')
  }

  stages {
    stage('Vault Login & Generate .env') {
      steps {
        sh '''
          echo "[INFO] Logging into Vault and generating .env file..."
          chmod +x ./scripts/vault_login.sh
          ./scripts/vault_login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
          ls -al ./app
          ls -al ./
          ls -al /scripts
        '''
        stash includes: 'app/.env', name: 'env-file'
      }
    }

    stage('Ansible Deploy') {
      steps {
        unstash 'env-file'
        sh 'mv .env app/.env'
        sh '''
          cd ansible
          ansible-playbook ./playbooks/deploy.yml \
            -i ./inventories/webs.ini \
            --private-key $PRIVATE_KEY
        '''
      }
    }
  }
}

