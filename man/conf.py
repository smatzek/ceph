import os

project = u'Ceph'
copyright = u'2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA'
version = 'dev'
release = 'dev'

exclude_patterns = ['**/.#*', '**/*~']

def _get_manpages():
    src_dir = os.path.dirname(__file__)
    top_srcdir = os.path.dirname(src_dir)
    man_dir = os.path.join(top_srcdir, 'doc', 'man')
    sections = os.listdir(man_dir)
    for section in sections:
        section_dir = os.path.join(man_dir, section)
        if not os.path.isdir(section_dir):
            continue
        for filename in os.listdir(section_dir):
            base, ext = os.path.splitext(filename)
            if ext != '.rst':
                continue
            if base == 'index':
                continue
            with file(os.path.join(section_dir, filename)) as f:
                one = f.readline()
                two = f.readline()
                three = f.readline()
                assert one == three
                assert all(c=='=' for c in one.rstrip('\n'))
                two = two.strip()
                name, rest = two.split('--', 1)
                assert name.strip() == base
                description = rest.strip()
            yield (
                os.path.join(section, base),
                base,
                description,
                '',
                section,
                )

man_pages = list(_get_manpages())
# sphinx warns if no toc is found, so feed it with a random file
# which is also rendered in this run.
master_doc = '8/ceph'
