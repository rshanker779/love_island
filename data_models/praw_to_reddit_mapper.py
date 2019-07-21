from praw.models import Comment, Submission, Redditor
import data_models.reddit_model as internal_model
from datetime import datetime


def get_comment(comment: Comment) -> internal_model.Comment:
    return internal_model.Comment(
        id=comment.id,
        submission_id=comment.submission.id,
        author_id=comment.author.id,
        author_flair_text=comment.author_flair_text,
        body=comment.body,
        created_utc=datetime.fromtimestamp(comment.created_utc),
        controversiality=comment.controversiality,
        depth=comment.depth,
        downs=comment.downs,
        gilded=comment.gilded,
        # We only populate parent if parent is another comment
        parent_id=comment.parent_id
        if comment.parent_id != comment.submission.fullname
        else None,
        permalink=comment.permalink,
        score=comment.score,
        score_hidden=comment.score_hidden,
        ups=comment.ups,
    )


def get_submission(submission: Submission) -> internal_model.Submission:
    return internal_model.Submission(
        id=submission.id,
        fullname=submission.fullname,
        title=submission.title,
        author_id=submission.author.id,
        author_flair_text=submission.author_flair_text,
        created_utc=datetime.fromtimestamp(submission.created_utc),
        distinguished=submission.distinguished,
        permalink=submission.permalink,
        score=submission.score,
        self_text=submission.selftext,
    )


def get_author(author: Redditor) -> internal_model.Author:
    return internal_model.Author(id=author.id, name=author.name)
