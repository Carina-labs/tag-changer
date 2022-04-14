import os
import yaml
from github import Github, InputGitAuthor
import base64


if __name__ == "__main__":
    gh_pat = os.getenv("INPUT_A41_PAT")
    dh_img_tag = os.getenv("INPUT_TAGS")
    g = Github(gh_pat)
    repo = g.get_repo("Carina-labs/helm-charts")
    contents = repo.get_contents(path="testnet/novachain-node/values.yaml", ref="test/img-update")
    v_yml = yaml.load(str(base64.b64decode(contents.content), 'utf-8'), Loader=yaml.Loader)
    v_yml['image']['tag'] = dh_img_tag
    new_vyml = yaml.dump(v_yml)
    bot = InputGitAuthor('github-actions[bot]', 'github-actions[bot]@users.noreply.github.com')
    repo.update_file(path=contents.path, message="Update my img tag",
                     content=new_vyml, sha=contents.sha, branch="test/img-update",
                     committer=bot)