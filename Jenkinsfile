pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
    KEY_FILE = credentials('GG_CLOUD_PRIVATE')
    SSH_CONFIG = credentials('SSH_CONFIG')
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
        sh '''
          echo "[INFO] Using SSH key"

          mkdir -p ~/.ssh
          chmod 700 ~/.ssh

          cp "$KEY_FILE" ~/.ssh/gg_cloud
          chmod 600 ~/.ssh/gg_cloud

          cp $SSH_CONFIG ~/.ssh/config
          cat ~/.ssh/config
          chmod 600 ~/.ssh/config

          echo "[INFO] Running Ansible playbook..."
          cd ansible
          ansible-playbook ./playbooks/deploy.yml -i ./inventories/webs.ini -vvvv
        '''
      }
    }
  }
}
