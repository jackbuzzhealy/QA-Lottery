pipeline{
        agent any
        stages{
            stage('get repo'){
                steps{
                    sh './scripts/get-repo.sh'
                }
	    stage('install docker'){
                steps{
                    sh './scripts/install-docker.sh'
                }
            stage('test service 1'){
                steps{
                    sh './scripts/test-service-1.sh'
                }
	    stage('test service 2'){
                steps{
                    sh './scripts/test-service-2.sh
                }
	    stage('test service 3'){
                steps{
                    sh './scripts/test-service-3.sh
                }
	    stage('test service 4'){
                steps{
                    sh './scripts/test-service-4.sh
                }
	    stage('deploy'){
                steps{
                    sh './scripts/deploy.sh
                }
            }
        }    
}
