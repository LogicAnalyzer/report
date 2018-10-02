pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				sh 'python3 generate.py'
			}
		}
		stage("Archive PDF"){
			steps{
				archiveArtifacts artifacts: 'report.pdf', fingerprint: true			
			}

		}
	}
}