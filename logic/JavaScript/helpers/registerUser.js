const { FetchWrapper } = require('./fetch_wrapper.mjs');

const registerUser = async (email, password, role) => {
  let userName = email.split('@')[0];
  const object = {
    email,
    password,
    role,
    username: userName,
  };

  const response = await new FetchWrapper(
    'https://example.com/users/register',
    {
      method: 'POST',
      body: JSON.stringify(object),
    }
  );
  return response;
};

module.exports = { registerUser };