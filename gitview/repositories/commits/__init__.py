from django.core.paginator import Paginator


class CommitPaginator(Paginator):

    def page(self, number):
        page = super(CommitPaginator, self).page(number)

        commits = page.object_list

        commits_day_data = {}

        for commit in commits:
            date = commit.committed_time.date()

            if not date in commits_day_data:
                commits_day_data[date] = []

            commits_day_data[date].append(commit)

        commits_list = []

        for commit in commits:
            date = commit.committed_time.date()

            if not date in commits_day_data:
                continue

            commits_list.append((date, commits_day_data[date]))

            del commits_day_data[date]

        page.object_list = commits_list

        return page
