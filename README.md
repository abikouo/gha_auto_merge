# Merging

## Branch protection rule [details](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

You can create a branch protection rule to enforce certain workflows for one or more branches, such as **requiring an approving review** or **passing status checks** for all pull requests merged into the protected branch.

You can create a branch protection rule in a repository for a specific branch, all branches, or any branch that matches a name pattern you specify with fnmatch syntax. _When you create a branch rule, the branch you specify doesn't have to exist yet in the repository_.

> Who can use this feature\_?
> People with admin permissions or a custom role with the "edit repository rules" permission to a repository can manage branch protection rules.

## Auto-merge [details](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request)

The pull request will merge automatically when all **required reviews** are met and all **required status checks have passed**.
**_Auto-merge must be enabled for the repository_**

After you enable auto-merge for a pull request, if **someone who does not have write permissions** to the repository **pushes new changes to the head branch or switches the base branch** of the pull request, **auto-merge will be disabled**.

[Managing auto-merge for pull requests in your repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository)
