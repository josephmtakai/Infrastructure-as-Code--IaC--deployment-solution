import os
import subprocess

def run_ansible_playbook(playbook):
    """Run an Ansible playbook."""
    try:
        subprocess.run(["ansible-playbook", playbook], check=True)
        print(f"Successfully ran {playbook}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {playbook}: {e}")

def main():
    """Main function to deploy infrastructure."""
    print("Starting infrastructure deployment...")
    
    # Run the main site.yml playbook
    run_ansible_playbook("ansible/playbooks/site.yml")

    print("Infrastructure deployment completed.")

if __name__ == "__main__":
    main()
