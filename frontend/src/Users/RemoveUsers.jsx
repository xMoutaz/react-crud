import React, { useCallback } from "react";

const deleteUsersBulk = async () => {
  await fetch("http://127.0.0.1:5000/users", {
    method: "DELETE",
  });
};

export default function RemoveUsers({ refetch }) {
  const onClick = useCallback(() => {
    deleteUsersBulk().then(refetch);
  }, [refetch]);
  return <button onClick={onClick}>Remove Users</button>;
}
