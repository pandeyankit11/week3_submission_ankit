from setuptools import setup

package_name = 'kratos_ankit'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ankit',
    maintainer_email='your@email.com',
    description='Assignment Q1 publisher/subscriber',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'q1_pub = kratos_ankit.q1_publisher:main',
        'q1_sub = kratos_ankit.q1_subscriber:main',
        'q2_pub = kratos_ankit.q2_publisher:main',
        'q2_con = kratos_ankit.q2_controller:main',
        'q3_pub = kratos_ankit.q3_publisher:main',
        'q3_sub = kratos_ankit.q3_subscriber:main',
        'q4_pub1 = kratos_ankit.q4_pub1:main',
        'q4_pub2 = kratos_ankit.q4_pub2:main',
        'q4_sub1 = kratos_ankit.q4_sub1:main',
        'q4_sub2 = kratos_ankit.q4_sub2:main',
        'q5_action_server = kratos_ankit.q5_action_server:main',
        'q5_action_client = kratos_ankit.q5_action_client:main',
        'q6_pub = kratos_ankit.q6_pub:main',
        'q6_sub = kratos_ankit.q6_sub:main',


    ],
},
)
