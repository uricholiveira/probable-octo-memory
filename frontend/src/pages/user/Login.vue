<template>
  <div>
    <div class="absolute-center" style="margin-top: -4rem">
      <div class="row justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
             style="height: 4rem">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"/>
        </svg>
      </div>
      <div class="row justify-center" style="margin-top: 0.1rem">
        <div class="col-12">
          <h4 style="font-size: 24px; text-align: center; font-weight: bolder">
            Enter with your account
          </h4>
        </div>
      </div>
      <div class="row" style="width: 320px;">
        <LoginForm/>
      </div>
      <div class="row" style="margin-top: 1rem; margin-bottom: -4rem">
        <div class="col-12 text-center">
          <p class="">or</p>
        </div>
        <div class="col-12 text-center" style="margin-bottom: 1rem">
          <router-link :to="{name: 'Register'}" class="animate-pulse text-amber-6 text-center">register</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from "components/user/forms/LoginForm";

export default {
  name: "Login",
  components: {LoginForm},
}
</script>

<style scoped>
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  text-decoration: none;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: .5;
  }

}
</style>
