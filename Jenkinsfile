pipeline {
    agent { label 'linux' } // Chú ý: dùng dấu nháy đơn ' ' cho label là tốt nhất
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '')
        disableConcurrentBuilds()
    }
    stages {
        stage('Hello') {
            steps {
                echo "hello"
            }
        }
    }
}
