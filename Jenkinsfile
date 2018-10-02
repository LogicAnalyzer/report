pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				sh '[ -e report.pdf ] && rm report.pdf"'
				sh 'python3 generate.py'
				archiveArtifacts artifacts: 'report.pdf', fingerprint: tru
			}
		}
	}
}