pipeline {
  agent any

  environment {
    VAULT_ADDR = credentials('VAULT_ADDR')
  }

  stages {
    stage('Debug') {
      steps {
        echo "Vault Addr: ${VAULT_ADDR}"
      }
    }
  }
}

