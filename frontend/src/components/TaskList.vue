<template>
<div>
  <q-list bordered class="rounded-borders">
    <q-expansion-item
      expand-separator
      default-opened
      icon="perm_identity"
      label="Today"
      caption="Activities due today"
    >
      <q-card>
        <q-card-section>
          <div class="row justify-around q-gutter-sm">
            <div class="col-xs-12 col-sm-10 col-md-6 col-lg-4">
              <q-card>
                <q-card-section class="q-gutter-y-sm" style="min-height: 160px; max-height: 160px">
                  <div class="row justify-start" style="font-weight: bold">
                    <div class="col-8">
                      Entregar app
                    </div>
                    <div class="col-4 text-right">
                      <q-badge label="Parado" color="primary" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col-8">
                      Desenvolvimento
                    </div>
                    <div class="col-4 text-right">
                      <q-badge label="Normal" color="positive" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col">
                      <q-badge label="28/02/2021" color="negative" />
                    </div>
                  </div>
                  <hr>
                  <div class="row justify-center">
                    <div class="col q-gutter-md text-center">
                      <q-btn dense padding="8px" unelevated label="Iniciar" size="sm" color="primary"/>
                      <q-btn dense padding="8px" unelevated label="Editar" size="sm" color="info"/>
                      <q-btn dense padding="8px" unelevated label="Concluir" size="sm" color="secondary"/>
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
    <q-expansion-item
      expand-separator
      icon="perm_identity"
      label="Tasks"
      caption="All task list"
    >
      <q-card>
        <q-card-section>
          <div class="row justify-around q-gutter-sm">
            <div class="col-xs-12 col-sm-10 col-md-6 col-lg-4">
              <q-card>
                <q-card-section class="q-gutter-y-sm" style="min-height: 160px; max-height: 160px">
                  <div class="row justify-start" style="font-weight: bold">
                    <div class="col-8">
                      Entregar app
                    </div>
                    <div class="col-4 text-right">
                      <q-badge label="Parado" color="primary" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col-8">
                      Desenvolvimento
                    </div>
                    <div class="col-4 text-right">
                      <q-badge label="Normal" color="positive" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col">
                      <q-badge label="28/02/2021" color="negative" />
                    </div>
                  </div>
                  <hr>
                  <div class="row justify-center">
                    <div class="col q-gutter-md text-center">
                      <q-btn dense padding="8px" unelevated label="Iniciar" size="sm" color="primary"/>
                      <q-btn dense padding="8px" unelevated label="Editar" size="sm" color="info"/>
                      <q-btn dense padding="8px" unelevated label="Concluir" size="sm" color="secondary"/>
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </q-list>
</div>
</template>

<script>
export default {
  name: "TaskList"
}
</script>

<style scoped>

</style>
