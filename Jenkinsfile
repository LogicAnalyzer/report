pipeline{
	agent any
	stages{
		stage("Update submodules"){
			steps{
				sh 'git submodule update --recursive --remote'
			}
		}
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