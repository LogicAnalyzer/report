pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				sh '[ -e report.pdf ] && rm report.pdf'
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