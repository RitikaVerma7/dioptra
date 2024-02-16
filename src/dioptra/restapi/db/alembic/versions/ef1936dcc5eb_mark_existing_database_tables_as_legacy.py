"""Mark existing database tables as 'legacy'

Revision ID: ef1936dcc5eb
Revises: 7086ad09e884
Create Date: 2024-02-09 10:57:16.378149

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "ef1936dcc5eb"
down_revision = "7086ad09e884"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("experiments", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_experiments_name"))

    with op.batch_alter_table("jobs", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_jobs_status"))
        batch_op.drop_index(batch_op.f("ix_jobs_queue_id"))
        batch_op.drop_index(batch_op.f("ix_jobs_mlflow_run_id"))
        batch_op.drop_index(batch_op.f("ix_jobs_experiment_id"))
        batch_op.drop_constraint(batch_op.f("fk_jobs_status_job_statuses"))
        batch_op.drop_constraint(batch_op.f("fk_jobs_queue_id_queues"))
        batch_op.drop_constraint(batch_op.f("fk_jobs_experiment_id_experiments"))

    with op.batch_alter_table("queues", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_queues_name"))

    with op.batch_alter_table("queue_locks", schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f("fk_queue_locks_queue_id_queues"))

    op.rename_table("experiments", "legacy_experiments")
    op.rename_table("jobs", "legacy_jobs")
    op.rename_table("queues", "legacy_queues")
    op.rename_table("users", "legacy_users")
    op.rename_table("job_statuses", "legacy_job_statuses")
    op.rename_table("queue_locks", "legacy_queue_locks")

    with op.batch_alter_table("legacy_experiments", schema=None) as batch_op:
        batch_op.create_index("ix_legacy_experiments_name", ["name"], unique=1)

    with op.batch_alter_table("legacy_jobs", schema=None) as batch_op:
        batch_op.create_index("ix_legacy_jobs_status", ["status"], unique=False)
        batch_op.create_index("ix_legacy_jobs_queue_id", ["queue_id"], unique=False)
        batch_op.create_index(
            "ix_legacy_jobs_mlflow_run_id", ["mlflow_run_id"], unique=False
        )
        batch_op.create_index(
            "ix_legacy_jobs_experiment_id", ["experiment_id"], unique=False
        )
        batch_op.create_foreign_key(
            batch_op.f("fk_legacy_jobs_status_legacy_job_statuses"),
            "legacy_job_statuses",
            ["status"],
            ["status"],
        )
        batch_op.create_foreign_key(
            "fk_legacy_jobs_queue_id_legacy_queues",
            "legacy_queues",
            ["queue_id"],
            ["queue_id"],
        )
        batch_op.create_foreign_key(
            "fk_legacy_jobs_experiment_id_legacy_experiments",
            "legacy_experiments",
            ["experiment_id"],
            ["experiment_id"],
        )

    with op.batch_alter_table("legacy_queues", schema=None) as batch_op:
        batch_op.create_index("ix_legacy_queues_name", ["name"], unique=1)

    with op.batch_alter_table("legacy_queue_locks", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_legacy_queue_locks_queue_id_legacy_queues",
            "legacy_queues",
            ["queue_id"],
            ["queue_id"],
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("legacy_experiments", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_legacy_experiments_name"))

    with op.batch_alter_table("legacy_jobs", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_legacy_jobs_status"))
        batch_op.drop_index(batch_op.f("ix_legacy_jobs_queue_id"))
        batch_op.drop_index(batch_op.f("ix_legacy_jobs_mlflow_run_id"))
        batch_op.drop_index(batch_op.f("ix_legacy_jobs_experiment_id"))
        batch_op.drop_constraint(
            batch_op.f("fk_legacy_jobs_status_legacy_job_statuses")
        )
        batch_op.drop_constraint(batch_op.f("fk_legacy_jobs_queue_id_legacy_queues"))
        batch_op.drop_constraint(
            batch_op.f("fk_legacy_jobs_experiment_id_legacy_experiments")
        )

    with op.batch_alter_table("legacy_queues", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_legacy_queues_name"))

    with op.batch_alter_table("legacy_queue_locks", schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f("fk_legacy_queue_locks_queue_id_legacy_queues")
        )

    op.rename_table("legacy_experiments", "experiments")
    op.rename_table("legacy_jobs", "jobs")
    op.rename_table("legacy_queues", "queues")
    op.rename_table("legacy_users", "users")
    op.rename_table("legacy_job_statuses", "job_statuses")
    op.rename_table("legacy_queue_locks", "queue_locks")

    with op.batch_alter_table("experiments", schema=None) as batch_op:
        batch_op.create_index("ix_experiments_name", ["name"], unique=1)

    with op.batch_alter_table("jobs", schema=None) as batch_op:
        batch_op.create_index("ix_jobs_status", ["status"], unique=False)
        batch_op.create_index("ix_jobs_queue_id", ["queue_id"], unique=False)
        batch_op.create_index("ix_jobs_mlflow_run_id", ["mlflow_run_id"], unique=False)
        batch_op.create_index("ix_jobs_experiment_id", ["experiment_id"], unique=False)
        batch_op.create_foreign_key(
            batch_op.f("fk_jobs_status_job_statuses"),
            "job_statuses",
            ["status"],
            ["status"],
        )
        batch_op.create_foreign_key(
            "fk_jobs_queue_id_queues", "queues", ["queue_id"], ["queue_id"]
        )
        batch_op.create_foreign_key(
            "fk_jobs_experiment_id_experiments",
            "experiments",
            ["experiment_id"],
            ["experiment_id"],
        )

    with op.batch_alter_table("queues", schema=None) as batch_op:
        batch_op.create_index("ix_queues_name", ["name"], unique=1)

    with op.batch_alter_table("queue_locks", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_queue_locks_queue_id_queues",
            "queues",
            ["queue_id"],
            ["queue_id"],
        )
    # ### end Alembic commands ###
