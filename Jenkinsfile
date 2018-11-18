pipeline{
	agent any
	stages{
		stage("Check Requirements"){
			steps{
				sh 'bash requirements.sh'
			}
		}
		stage("Spell Check"){
			steps{
				sh 'python3 spell_check.py'
				junit '*.xml'
			}
		}
		stage("Create PDF"){
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